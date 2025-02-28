import timeit
import numpy as np
import matplotlib.pyplot as plt
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0;

    def display(self):
        ptr = self.head
        while ptr != None:
            print(ptr.data, end=' > ')
            ptr = ptr.next

    def fill(self, size):
        for i in range(size, 0, -1):
            self.insert(Node(i))

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
                low = mid.next
class Array:
    def __init__(self):
        self.data = []
        self.count = 0

    def fill(self, size):
        for i in range(1, size + 1):
            self.push(i)

    def push(self, value):
        self.data.append(value)
        self.count += 1

    def binary_search(self, key):
        self.data = np.array(self.data)
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

def plot(x, y1, y2):
    x = np.array(x)
    x_logged = np.log(x)
    a1, b1 = np.polyfit(x_logged, y1, 1)
    y1_pred = a1 * np.log(x) + b1

    a2, b2 = np.polyfit(x, y2, 1)
    y2_pred = a2 * x + b2

    plt.scatter(x, y1, color='red', label='Array')
    plt.plot(x, y1_pred, color='purple', label="Array (Interpolated)")
    plt.scatter(x, y2, color='blue', label='Linked List')
    plt.plot(x, y2_pred, color='green', label="Linked List (Interpolated)")
    plt.title("Execution time for Binary Search on Arrays and Linked Lists of varying sizes")
    plt.xlabel("Input size")
    plt.ylabel("Execution time (seconds)")
    plt.legend()
    plt.savefig("ex1.png")


def test_search():
    array_times = []
    llist_times = []
    sizes = [1000, 2000, 4000, 8000]
    for size in sizes:
        key = random.randint(size * 2 // 7, size * 3 // 7)
        array = Array()
        array.fill(size)
        array_time = timeit.timeit(lambda: array.binary_search(key), number=10)
        array_times.append(array_time / 10)

        list = LinkedList()
        list.fill(size)
        llist_time = timeit.timeit(lambda: list.binary_search(key), number=10)
        llist_times.append(llist_time / 10)
        
    plot(sizes, array_times, llist_times)

test_search()

# 4. What is the complexity of binary search for linked lists?
# The complexity of binary search for linked lists is O(n) (linear). This is because the middle element has to be calculated
# in linear time by traversing the list on each iteration. So despite halving the array on each iteration of the loop, the 
# linear time complexity of the get_middle function prevents it from being O(logn) like array binary search, which can
# find the middle in O(1) time.
