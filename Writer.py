import io
import json

import Shared
from Node import *


class Writer:

    def __init__(self, depth):
        self.nodeByWords = {}

    def load(self, path):
        data = None
        with io.open(path, mode="r", encoding="utf-8") as file:
            data = json.load(file)

        for key, nodeData in data.items():
            node = Node(key)
            self.nodeByWords[key] = node

            for word, count in nodeData.items():
                next_node = Shared.get_or_create_node(self.nodeByWords, [word])
                node.countByNextNode[next_node] = count

    def write(self, path):
        pass


