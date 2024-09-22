# MedKit

A repo for revisiting data structure and algorithms.

## Sorting

This section we solve most famous sort algorithms. You can find the algorithm description in the external links.

- [Bubble Sort](https://www.geeksforgeeks.org/bubble-sort/)
- [Selection Sort](https://www.geeksforgeeks.org/selection-sort-algorithm-2/)
- [Insertion Sort](https://www.geeksforgeeks.org/insertion-sort/)
- [Merge Sort](https://www.geeksforgeeks.org/merge-sort/)
- [Quick Sort]()

## Graph Shortest Path

- [Dijkstra](https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php)
- [Bellman-ford](https://www.w3schools.com/dsa/dsa_algo_graphs_bellmanford.php)

## Data Structure

Some of the most used data structure implementation using python.

- array
- graph
- stack
- queue
- linked-list
- tree

### Tree data structure

1. Binary Tree
   A tree data structure where each node has at most two children referred to as the left child and the right child.

Use Cases:

- Basic hierarchical data representation
- Parsing expressions (e.g., in compilers)

Key Operations

- Insert: Add a new node to the binary tree.
- Inorder Traversal: Visit nodes in the left-root-right order. Useful for binary search trees to retrieve sorted elements.
- Preorder Traversal: Visit nodes in the root-left-right order. Useful for copying the tree.
- Postorder Traversal: Visit nodes in the left-right-root order. Useful for deleting the tree.
- Level Order Traversal: Visit nodes level by level from left to right. Useful for breadth-first search.
  This basic implementation of a binary tree in Python includes methods for insertion and different types of tree traversal.
  The level_order method uses a queue to perform a breadth-first traversal of the tree.

2. Binary Search Tree (BST)
   A binary tree with the property that the left child of a node contains a value less than the node’s value,
   and the right child contains a value greater than the node’s value.

Use Cases:

- Efficient searching, insertion, and deletion operations
- Used in databases and file systems

3. AVL Tree
   A self-balancing binary search tree where the difference between the heights of left and right subtrees cannot be
   more than one for all nodes.

Use Cases:

- When balanced tree operations are required
- Useful in databases and caches where insert/delete operations are frequent

4. Red-Black Tree
   A self-balancing binary search tree where nodes can be red or black, ensuring the tree remains balanced.

Use Cases:

- Used in many data structures like TreeMap, TreeSet in Java
- Linux kernel uses it for memory management

5. B-Tree
   A self-balancing search tree where nodes can have more than two children, commonly used in databases and file systems.

Use Cases:

- Efficient for reading/writing large blocks of data
- Widely used in databases and filesystems (e.g., NTFS, SQLite)

6. Trie (Prefix Tree)
   A tree-like data structure that stores a dynamic set of strings, where the keys are usually strings.

Use Cases:

- Efficiently store and retrieve keys in a dataset of strings
- Autocomplete and spell-checking applications

7. Segment Tree
   A binary tree used for storing intervals or segments. It allows querying which of the stored segments contain a given point.

Use Cases:

- Range query problems
- Computational geometry applications

8. Fenwick Tree (Binary Indexed Tree)
   A data structure that provides efficient methods for calculation and manipulation of the prefix sums of a table of values.

Use Cases:

- Used in scenarios involving frequent cumulative frequency table updates
- Competitive programming for solving range sum queries efficiently

9. N-ary Tree
   A tree where each node can have up to N children.

Use Cases:

- Representing hierarchies with more than two children (e.g., file systems, organizational structures)
