from typing import List


# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def depth_first_search(self, array: List[str]) -> List[str]:
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
