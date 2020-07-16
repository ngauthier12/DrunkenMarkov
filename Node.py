

class Node:

    def __init__(self, text):
        self.text = text
        self.countByNextNode = {}

    def increment(self, node):
        count = self.countByNextNode(node, 0)
        self.countByNextNode[node] = ++count
        print(self.text + " => " + node.text + " : " + count)
