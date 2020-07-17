

class Node:

    def __init__(self, key):
        self.key = key
        self.countByNextNode = {}

    def increment(self, node):
        count = self.countByNextNode.get(node, 0)
        count += 1
        self.countByNextNode[node] = count
