import io
import json

import Shared
from Node import *


class Writer:

    def __init__(self, depth):
        self.nodeByWords = {}
        self.wordCount = 0

    def load(self, path):
        root = None
        with io.open(path, mode="r", encoding="utf-8") as file:
            root = json.load(file)

        self.wordCount = root["wordCount"]
        print("wordCount: " + str(self.wordCount))

        data = root["data"]
        for key, nodeData in data.items():
            node = Node(key)
            self.nodeByWords[key] = node

            for word, count in nodeData.items():
                next_node = Shared.get_or_create_node(self.nodeByWords, [word])
                node.countByNextNode[next_node] = count

    def write(self, path):
        pass


