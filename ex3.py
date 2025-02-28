import sys
import timeit
import matplotlib.pyplot as plt

"""
Question 1: Identify and explain the strategy used to grow arrays when full, with references to specific lines of code in the file above. What is the growth factor?

if (allocated >= newsize && newsize >= (allocated >> 1))

When the number of allocated memory is enough to store a new element, it simply sets the size to the new size with the call: Py_SET_SIZE(self, newsize).


new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;

The growth factor is determined by the above statement, using the bitwise shift, and, and not operators which is not constant but varies depending on the new_size. From testing, the growth factor seems to converge around 1.125 for large lists but can be very different at samller sizes.
"""

# 2
def print_growing_capacity():
    array = []
    for i in range(63):
        old_capacity = sys.getsizeof(array)
        array.append(i)
        new_capacity = sys.getsizeof(array)
        if new_capacity > old_capacity:
            print(f"Size: {i}=>{i + 1}\tCap (bytes): {old_capacity}=>{new_capacity}\tGrowth: {new_capacity/old_capacity}")

# 3/4: S is 52
def grow_array(array):
    array.append(1)

def setup_array(n):
    array = []
    for i in range(n):
        array.append(i)
    return array

def test_S_growth():
    S = 52
    times_growth_over = []
    times_growth_under = []
    iterations = 1
    for i in range(1000):
        arr1 = []
        for j in range(S):
            arr1.append(j)
        arr2 = []
        for j in range(S-1):
            arr2.append(j)
        time_over = timeit.timeit(lambda: arr1.append(1), number=iterations) / iterations
        times_growth_over.append(time_over)
        time_under = timeit.timeit(lambda: arr2.append(1), number=iterations) / iterations
        times_growth_under.append(time_under)
    plot(times_growth_under, times_growth_over)

def plot(d1, d2):
    fig, axs = plt.subplots(1, 2, tight_layout=True)
    bins = 100
    axs[0].hist(d1, range=[0, 1e-6], bins=bins)
    axs[1].hist(d2, range=[0, 1e-6], bins=bins)
    axs[0].set_title("S-1 to S")
    axs[1].set_title("S to S+1")
    plt.savefig("ex3.png")


print_growing_capacity()
test_S_growth()

# 5. Do you see any difference? Why?
"""
The distribution of the array that goes from S-1 to S is shifted over to the left a small amount compared to the graph that goes from S to S+1.
This is cased by the array having to resize its capacity in the second case which takes more time than the first case which does not have to deal with that. The difference is pretty marginal likely due to the fact that the array is quite small and reallocating space/copying elements would not take a very significant amount of time.
"""
