import io
import json

from Tokenizer import *
from Node import *


class Parser:

    def __init__(self):
        tokenizer = Tokenizer()
        tokenizer.on_word = lambda x: self.__on_word(x)
        self.tokenizer = tokenizer

        root = Node("")
        self.nodeByText = {"": root}
        self.lastNode = root

    def read(self, path):
        with io.open(path, mode="r", encoding="utf-8") as file:
            text = file.read()
        print("parsing " + path + " of len: " + str(len(text)))
        self.tokenizer.read(text)

    def save(self, path):
        map_node = lambda node: node.text
        map_junction = lambda node: dict(zip(map(map_node, node.countByNextNode.keys()), node.countByNextNode.values()))
        data = dict(zip(self.nodeByText.keys(), map(map_junction, self.nodeByText.values())))
        print("saving data (json) at: " + path)

        with io.open(path, mode="w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def __on_word(self, word):
        if word in self.nodeByText:
            node = self.nodeByText[word]
        else:
            node = Node(word)
            self.nodeByText[word] = node

        self.lastNode.increment(node)
        self.lastNode = node
