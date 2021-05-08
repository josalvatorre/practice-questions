# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def breadth_first_search(self, array):
        # BFS is FIFO order traverse, so we'll use a queue
        node_queue = [self]
        while 0 < len(node_queue):
            # dequeue
            node = node_queue.pop(0)
            # record this name
            array.append(node.name)
            # enqueue all children
            node_queue.extend(node.children)
        return array
