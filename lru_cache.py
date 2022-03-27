import dataclasses
from typing import Optional, Tuple


@dataclasses.dataclass
class Node:
    key: str
    value: int
    next_: Optional["Node"]
    prev: Optional["Node"]


@dataclasses.dataclass(frozen=True)
class Queue:
    head: Optional[Node]
    tail: Optional[Node]


# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, max_size):
        self.maxSize = max_size or 1
        self.map = {}
        self.queue = Queue(None, None)

    @staticmethod
    def enqueue(q: Queue, key: str, value: int) -> Tuple[Queue, Node]:
        node = Node(key=key, value=value, prev=None, next_=q.head)
        # empty queue
        if q.head is q.tail is None:
            return Queue(head=node, tail=node), node
        else:
            assert q.head is not None
            assert q.tail is not None
            q.head.prev = node
            return Queue(head=node, tail=q.tail), node
        pass

    @staticmethod
    def remove(q: Queue, node: Node) -> Queue:
        assert q.head is not None
        assert q.tail is not None
        assert node is not None

        if node is q.head:
            head = node.next_
            if head is not None:
                head.prev = None
        else:
            # keep the head
            head = q.head
            # If node isn't the head, then it must have a previous element.
            node.prev.next_ = node.next_

        if node is q.tail:
            tail = node.prev
            if tail is not None:
                tail.next_ = None
        else:
            # keep the tail
            tail = q.tail
            # if node isn't the tail, then it must have a next element
            node.next_.prev = node.prev

        return Queue(head=head, tail=tail)

    def insert_key_value_pair(self, key: str, value: int) -> None:
        node = self.map.get(key)
        if node is None:
            # we have to evict before adding a new value
            if self.maxSize <= len(self.map):
                # dequeue
                evicted = self.queue.tail
                self.queue = self.remove(self.queue, evicted)
                self.map.pop(evicted.key)
                pass
            self.queue, node = self.enqueue(self.queue, key, value)
            self.map[key] = node
        else:
            self.queue = self.remove(self.queue, node)
            self.queue, node = self.enqueue(self.queue, key, value)
            self.map[key] = node
        pass

    def get_value_from_key(self, key) -> Optional[int]:
        node = self.map.get(key)
        if node is None:
            return None
        self.queue = self.remove(self.queue, node)
        self.queue, node = self.enqueue(self.queue, key, node.value)
        self.map[key] = node
        return node.value

    def get_most_recent_key(self) -> Optional[str]:
        if self.queue.head is None:
            return None
        return self.queue.head.key
