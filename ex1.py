class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0;

    def insert(self, node):
        node.next = self.head
        self.head = node
        self.count += 1

    def node_at(self, i):
        node = self.head
        for i in range(i):
            if node == None:
                return None
            node = node.next
        return node
    def node_from(self, node_guard, i):
        ptr = self.head
        while ptr != node_guard:
            ptr = ptr.next

        for i in range(i):
            if ptr == None:
                return None
            ptr = ptr.next
        return ptr

    def get_middle(self, low, high):
        if low == None:
            return None
        if low == high:
            return low

        offset = 0;
        ptr = low
        while ptr != high:
            ptr = ptr.next
            offset += 1
        return self.node_from(low, offset//2)

    def binary_search(self, key):
        low = self.head
        high = self.node_at(self.count - 1)
        while True:
            mid = self.get_middle(low, high)
            if mid is None:
                return False
            elif mid.data == key:
                return True
            elif low == high:
                return False
            elif key < mid.data:
                high = mid
            elif key > mid.data:
                low = self.node_from(mid, 1)
class Array:
    def __init__(self):
        self.data = []
        self.count = 0

    def push(self, value):
        self.data.append(value)
        self.count += 1

    def binary_search(self, key):
        low = 0
        high = self.count - 1
        while low <= high:
            mid = (low + high) // 2
            value = self.data[mid]
            if key == value:
                return mid
            elif low == high:
                return -1
            elif key < value:
                high = mid - 1
            elif key > value:
                low = mid + 1


def test_search():
    list = LinkedList()
    list.insert(Node(5))
    list.insert(Node(4))
    list.insert(Node(3))
    list.insert(Node(2))
    list.insert(Node(1))
    print(list.binary_search(5))

    array = Array()
    array.push(1)
    array.push(2)
    array.push(3)
    array.push(4)
    array.push(19)
    print(array.binary_search(18))
    print(array.binary_search(19))

test_search()
