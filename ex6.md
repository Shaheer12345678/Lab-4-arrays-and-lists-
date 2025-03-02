# 1.
## Element access:
- Array can access elements in O(1) due to their contiguous memory layout\
- Linked lists have an average case access complexity of O(n) since they need to linearly iterate through the list to find a given value.

## Insertion/Deletion
- Arrays must shift elements over to the left or right if inserting/deleting an element not at the end of their block of memory. This results in an average case complexity of O(n). They may also need to reallocate memory and do some copying which is not reflected in the complexity but does have a performance impact.
- Linked lists have an average case insertion/deletion complexity of O(n), but they are more efficient than arrays for inserting at or near the beginning of the list, or at the end if a tail pointer is involved. Specifically, insertion and deletion at the beginning of the list (or at the end with a tail pointer) has a complexity of O(1).

# 2.
- prevNode : Node at the index before the newNode
- newNode : Node to be inserted
- oldNode : Node to be replaced/deleted
- Iterate to prevNode
- newNode can be created/allocated
- newNode.next = oldNode.next
- oldNode can be deallocated
- prevNode.next = newNode\
This avoids unnecessary iteration.

# 3.
1. Insertion sort
It is feasible to implement insertion sort for a doubly linked list.\
It is important to be able to iterate backwards for insertion sort to be\
able to move the key to the proper position in the list, and since\
we are working with a doubly linked list this is possible.

2. Merge sort
It is also possible to implement a merge sort for a doubly-linked list\
To be able to implement merge sort, it is necessary to be able to divide\
the list in half on each recursion call. This can be done with a linked list,\
albeit in a different way than in an array which has the benefit of having random\
access making it possible to do this division using low and high indices. In a\
linked list the algorithm must split the list into two parts before calling merge\
sort on both parts and finally merging the parts back together.

# 4.
1. Insertion sort
The expected complexity of insertion sort on a doubly linked list would not be any different\
compared to an array, meaning a complexity of $O(n^2)$, $O(n^2)$, $O(n)$ for the worst, average,\
and best case complexities.\
\
How this complexity is found:\
- Outer loop linearly iterates through list. (same as array)
- Inner loop linearly shifts key backwards through the list.
    - In an array this is done by shifting elements over
    - In a linked list this is done by juggling pointers
    - The complexity of both is linear
- If the list/array is already sorted no swaps will be done, resulting in $O(n)$

2. Merge sort
The expected complexity of merge sort on a doubly linked list would also not be any different\
from the complexity of an array. In all cases, a properly implemented merge sort would have a\
complexity of $O(n log n)$.\
\
How this complexity is found:\
- Midpoint must be found to divide the list into two parts:
    - In an array this is done with a simple calculation (often (low + high) // 2). This is done in constant time.
    - In a doubly linked list this can be done by splitting the list into two parts (setting the next pointer of first half to None). This is done in linear time.
- Merge sort is called recursively on both halves of the list:
    - The recursion depth for both an array and a linked list would be $log_2 n$ , since both divide the list into the same sized chunks.
- Subarrays are merged together:
    - This is done in linear time for both an array and a linked list, since in both algorithms it iterates through each element of the subarray once, placing the lower on into the merged list until all elements are placed.
- The logarithmic recursive calls and the linear merges result in a log linear complexity in both cases. The reason that the additional O(n) midpoint calculation in the linked list does not make the complexity worse than log linear is because coefficients do not matter in complexity analysis, so 2 linear complexity functions (2n) will just be rounded to (n).
