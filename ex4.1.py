def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2

# 1. State and justify what is the best, worst and average case complexity for the code in the previous slide.
"""
Best case: O(n)
In the best case, li[i] > 5 never evaluates to true, meaning the funciton only has to iterate linearly through the data with the first for loop.


Average case: O(n^2)
In the average case, li[i] > 5 evaluates to true half the time, meaning both for loops will end up running. To oversimplify for brevity: O(n * n/2) => O(n^2)

Worst case: O(n^2)
In the worst case, li[i] > 5 always evaluates to true, meaning both for loops run the maximum length. They are both O(n) so the two of them result in a complexity of O(n^2)

"""

# 2. Are average, best, and worst case complexity the same? If not, produce a modified version of the code above for which average, best, and worst case complexity are equivalent.
"""
They are not.
Average and worst cases are the same, but best case is not the same.
"""

def modified_processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            li[i] *= 2 ** len(li)
