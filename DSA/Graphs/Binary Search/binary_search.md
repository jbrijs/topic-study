# Binary Search

Binary Search is a searching algorithm that can be used to find an element in a sorted list. Like the name implies, on each iteration, or recursive call, it splits the search space in two. It looks at the midpoint, compares it to the desired element, and then continues on the half of the list that could contain the element. It can be written recursively or iteratively. 

### Time complexity

Binary Search has time complexity of O(log(n)), where n is the length of the input array. It is O(log(n)) because the search space is decreased from n, n/2, n/4, ... n/n.

