import io
import json

import Shared
from Node import *


class Writer:

    def __init__(self,):
        self.nodeByWords = {}
        self.wordCount = 0
        self.depth = 0

    def load(self, path):
        root = None
        with io.open(path, mode="r", encoding="utf-8") as file:
            root = json.load(file)

        self.wordCount = root["wordCount"]
        print("wordCount: " + str(self.wordCount))

        self.depth = max(self.depth, root["depth"])
        print("depth: " + str(self.depth))

        data = root["data"]
        for key, nodeData in data.items():
            node = Node(key)
            self.nodeByWords[key] = node

            for word, count in nodeData.items():
                next_node = Shared.get_or_create_node(self.nodeByWords, [word])
                node.countByNextNode[next_node] = count

    def write(self, path):
        first = Shared.get_or_create_node(self.nodeByWords, [""])
        nodes = [first]

        for i in range(self.wordCount):
            choices = self.__get_next_node_from_history(nodes)
            node = choices.get_random_next()
            nodes.append(node)

        words = map(lambda node: node.key, nodes)
        text = " ".join(words)

        print("writing text at: " + path + " of len: " + str(len(text)))

        with io.open(path, mode="w", encoding="utf-8") as file:
            file.write(text)

    def __get_next_node_from_history(self, history):
        for n in range(self.depth, 1, -1):
            word_list = list(map(lambda node: node.key, history[-n:]))
            node = Shared.try_get_node(self.nodeByWords, word_list)
            if node is not None:
                return node
        print("no node found in history for: '" + history[-1].key + "'")
        print(history[-1:])
        return None
