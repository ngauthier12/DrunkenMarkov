from Node import *


def make_key(word_list):
    return " ".join(word_list)


def get_or_create_node(dictionary, word_list):
    key = make_key(word_list)
    if key in dictionary:
        node = dictionary[key]
    else:
        node = Node(key)
        dictionary[key] = node
    return node


def try_get_node(dictionary, word_list):
    key = make_key(word_list)
    if key in dictionary:
        return dictionary[key]
    return None
