import io
import json

import Shared
from Tokenizer import *
from Node import *


class Parser:

    def __init__(self, depth):
        tokenizer = Tokenizer()
        tokenizer.on_word = lambda x: self.__on_word(x)
        self.tokenizer = tokenizer

        root = Node(Shared.make_key([""]))
        self.nodeByWords = {root.key: root}
        self.depth = depth
        self.history = [root]
        self.wordCount = 0

    def read(self, path):
        with io.open(path, mode="r", encoding="utf-8") as file:
            text = file.read()
        print("parsing " + path + " of len: " + str(len(text)))
        self.tokenizer.read(text)

    def save(self, path):
        map_node = lambda node: node.key
        map_junction = lambda node: dict(zip(map(map_node, node.countByNextNode.keys()), node.countByNextNode.values()))
        data = dict(zip(self.nodeByWords.keys(), map(map_junction, self.nodeByWords.values())))
        print("saving data (json) at: " + path + " of len: " + str(len(data)))

        root = {}
        root["data"] = data
        root["wordCount"] = self.wordCount

        with io.open(path, mode="w", encoding="utf-8") as file:
            json.dump(root, file, indent=4)

    def __on_word(self, word):
        current = Shared.get_or_create_node(self.nodeByWords, [word])

        for i in range(self.depth):
            previous_nodes = self.history[i:]
            previous_words = map(lambda node : node.key, previous_nodes)
            previous_node = Shared.get_or_create_node(self.nodeByWords, previous_words)
            previous_node.increment(current)

        self.history.append(current)

        if len(self.history) > self.depth:
            self.history.pop(0)

        self.wordCount += 1
