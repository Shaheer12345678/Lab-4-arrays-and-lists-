import timeit
import matplotlib.pyplot as plt
import random

# 3. Provide the code for an inefficient implementation and an efficient implementation.
def inefficient(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i

def efficient(array, target):
    low = 0
    high = len(array) - 1
    while low < high:
        mid = (low + high) // 2
        value = array[mid]

        if target == value:
            return mid
        elif target < value:
            high = mid - 1
        else:
            low = mid + 1

# 4. State the worst case complexity of each.
"""
Worst case complexity of inefficient search:
O(n) : target is not in the array

Worst case complexity of efficient search:
O(logn) : target is not in the array
"""

# 5. Provide the code for an experiment that demonstrates the difference.
    #   1. Time the execution of both implementations on realistic, large inputs (1000 elements or above)
def experiment():
    inefficient_measurements = []
    efficient_measurements = []
    size = 2000
    array = [x for x in range(size)]
    for i in range(200):
        target = random.randint(-1, size)

        time_inefficient = timeit.timeit(lambda: inefficient(array, target), number=10) / 10
        inefficient_measurements.append(time_inefficient)

        time_efficient = timeit.timeit(lambda: efficient(array, target), number=10) / 10
        efficient_measurements.append(time_efficient)
    plot(inefficient_measurements, efficient_measurements)

    #   2. Plot the distribution of measured values across multiple measurements (>= 100 measurements per task)
def plot(d1, d2):
    fig, axs = plt.subplots(1, 2, tight_layout=False)
    fig.set_figwidth(16)
    bins = 50
    axs[0].hist(d1, bins=bins)
    axs[1].hist(d2, bins=bins)
    axs[0].set_title("Inefficient sort")
    axs[1].set_title("Efficient sort")
    plt.savefig("ex4.2.png")

experiment()
