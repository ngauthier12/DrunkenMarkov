import io

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
        file = io.open(path, mode="r", encoding="utf-8")
        text = file.read()
        print("parsing " + path + " of len: " + str(len(text)))
        self.tokenizer.read(text)

    def save(self, path):
        pass

    def __on_word(self, word):
        node = None
        if word in self.nodeByText:
            node = self.nodeByText[word]
        else:
            node = Node(word)
            self.nodeByText[word] = node

        self.lastNode.increment(node)
        self.lastNode = node
