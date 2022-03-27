from typing import Callable, Optional


# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        values = []
        node = self.head
        while node is not None:
            values.append(node.value)
            node = node.next
        return " -> ".join(map(str, values))

    def _find_by(self, is_target: Callable[[Node], bool]) -> Optional[Node]:
        node = self.head
        while node is not None:
            if is_target(node):
                return node
            node = node.next
        return None

    def _find_same(self, node: Node) -> Optional[Node]:
        return self._find_by(is_target=lambda n: n is node)

    def _find(self, value: int) -> Optional[Node]:
        return self._find_by(is_target=lambda n: n.value == value)

    def _insert_before(self, node: Node, node_to_insert: Node) -> None:
        """
        Assumes that:
        * node is in the list
        * nodeToInsert is not in the list
        """
        if node is self.head:
            # START: None <- node
            # END:   None <- nodeToInsert <-> node
            # END:   self.head = nodeToInsert

            # None <- nodeToInsert
            node_to_insert.prev = None
            #
            self.head = node_to_insert
            # defer: nodeToInsert <-> node
        else:
            # START: node.prev <-> node
            # END:   node.prev <-> nodeToInsert <-> node

            # node.prev <-> nodeToInsert
            node.prev.next, node_to_insert.prev = node_to_insert, node.prev
            # defer: nodeToInsert <-> node

        # nodeToInsert <-> node
        node_to_insert.next, node.prev = node, node_to_insert
        pass

    def _insert_after(self, node, node_to_insert) -> None:
        """
        Assumes that:
        * node is in the list
        * nodeToInsert is not in the list
        """
        if node is self.tail:
            # START: node -> None
            # END:   node <-> nodeToInsert -> None
            # END:   self.tail = nodeToInsert

            # nodeToInsert -> None
            node_to_insert.next = None
            #
            self.tail = node_to_insert
            # defer: node <-> nodeToInsert
        else:
            # START: node <-> node.next
            # END:   node <-> nodeToInsert <-> node.next

            # nodeToInsert <-> node.next
            node_to_insert.next, node.next.prev = node.next, node_to_insert
            # defer: node <-> nodeToInsert

        # # node <-> nodeToInsert
        node.next, node_to_insert.prev = node_to_insert, node
        pass

    def _remove(self, node) -> None:
        """
        Assumes that node is in list.
        """
        if node is self.head is self.tail:
            # START: None <- node -> None
            # END:   self.head = self.head = None
            self.head = self.tail = None
            return None

        elif node is self.head:
            # START: None <- node <-> node.next
            # END:   None <- node -> None
            # END:   None <- node.next
            # END:   self.head = node.next

            # None <- node.next
            node.next.prev = None
            #
            self.head = node.next

        elif node is self.tail:
            # START: node.prev <-> node -> None
            # END:   node.prev -> None
            # END:   None <- node -> None
            # END:   self.tail = node.prev

            # node.pev -> None
            node.prev.next = None
            #
            self.tail = node.prev

        else:
            # START: node.prev <-> node <-> node.next
            # END:   node.prev <-> node.next
            # END:   None <-> node <-> None

            # node.prev <-> node.next
            node.prev.next, node.next.prev = node.next, node.prev

        # None <-> node <-> None
        node.prev = node.next = None
        pass

    def set_head(self, node: Node) -> None:
        existing_node = self._find_same(node=node)
        if existing_node is self.head is not None:
            print(self)
            return None
        # if node is not in list
        if existing_node is None:
            # make sure it's a clean node
            node.prev = node.next = None
        else:
            # remove before inserting
            self._remove(node=existing_node)

        if self.head is None:
            self.head = self.tail = node
        else:
            self._insert_before(node=self.head, node_to_insert=node)
        print(self)
        pass

    def set_tail(self, node: Node) -> None:
        existing_node = self._find(value=node.value)
        if existing_node is self.tail is not None:
            print(self)
            return None
        # if node is not in list
        if existing_node is None:
            # make sure it's a clean node
            node.prev = node.next = None
        else:
            # remove before inserting
            self._remove(node=existing_node)

        if self.tail is None:
            self.head = self.tail = node
        else:
            self._insert_after(node=self.tail, node_to_insert=node)
        print(self)
        pass

    def insert_before(self, node, node_to_insert):
        existing_node = self._find_same(node=node_to_insert)
        if existing_node is not None:
            self._remove(node=existing_node)

        self._insert_before(node=node, node_to_insert=node_to_insert)
        print(self)
        pass

    def insert_after(self, node, node_to_insert):
        existing_node = self._find_same(node=node_to_insert)
        if existing_node is not None:
            self._remove(node=existing_node)

        self._insert_after(node=node, node_to_insert=node_to_insert)
        print(self)
        pass

    def insert_at_position(self, position, node_to_insert):
        if position == 1 and self.head is None:
            self.head = self.tail = node_to_insert
            print(self)
            return
        # Before altering the list,
        # find the already-existing node to remove later.
        existing_node = self._find_same(node=node_to_insert)
        i = 1
        node = self.head
        while i < position and node is not None:
            node = node.next
            i += 1

        if existing_node is not None:
            self._remove(node=existing_node)
        if node is not None:
            self._insert_before(node=node, node_to_insert=node_to_insert)
        print(self)
        pass

    def remove(self, node):
        existing_node = self._find_same(node=node)
        if existing_node is None:
            print(self)
            return
        else:
            self._remove(node=existing_node)
        print(self)
        pass

    def remove_nodes_with_value(self, value):
        existing_node = self._find(value=value)
        while existing_node is not None:
            self._remove(node=existing_node)
            existing_node = self._find(value=value)
        print(self)
        pass

    def contains_node_with_value(self, value) -> bool:
        print(self)
        return self._find(value=value) is not None
