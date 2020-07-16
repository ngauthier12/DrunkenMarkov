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
        file = open(path, "r")
        text = file.read()
        self.tokenizer.read(text)

    def save(self, path):
        pass

    def __on_word(self, word):
        node = self.nodeByText.get(word, Node(word))
        self.lastNode.increment(node)
