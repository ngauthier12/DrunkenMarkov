import random

random.seed(1337)

class Node:

    def __init__(self, key):
        self.key = key
        self.countByNextNode = {}

    def increment(self, node):
        count = self.countByNextNode.get(node, 0)
        count += 1
        self.countByNextNode[node] = count

    def get_random_next(self):
        choices = list(self.countByNextNode.keys())
        weights = list(self.countByNextNode.values())
        return random.choices(population=choices, weights=weights)[0]
