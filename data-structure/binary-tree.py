"""
Binary Tree
   A tree data structure where each node has at most two children referred to as the left child and the right child.

Use Cases:

- Basic hierarchical data representation
- Parsing expressions (e.g., in compilers)

2. Binary Search Tree (BST)
   A binary tree with the property that the left child of a node contains a value less than the node’s value,
   and the right child contains a value greater than the node’s value.

Use Cases:

- Efficient searching, insertion, and deletion operations
- Used in databases and file systems

Key Operations

- Insert: Add a new node to the binary tree.
- Inorder Traversal: Visit nodes in the left-root-right order. Useful for binary search trees to retrieve sorted elements.
- Preorder Traversal: Visit nodes in the root-left-right order. Useful for copying the tree.
- Postorder Traversal: Visit nodes in the left-right-root order. Useful for deleting the tree.
- Level Order Traversal: Visit nodes level by level from left to right. Useful for breadth-first search.
  This basic implementation of a binary tree in Python includes methods for insertion and different types of tree traversal.
  The level_order method uses a queue to perform a breadth-first traversal of the tree.

"""

from collections import deque
from typing import Tuple, Iterable, Union


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = TreeNode(data)
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = TreeNode(data)

    def inorder(self, node: TreeNode):
        # left-root-right
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node: TreeNode):
        # root-left-right
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node: TreeNode):
        # left-right-root
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def level_order(self):
        if not self.root:
            print("Tree is empty")
            return

        queue = deque()
        queue.append(self.root)

        while queue:
            current_node = queue.popleft()
            print(current_node.data, end=" ")

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    def search(self, key, parent=False) -> Iterable[Union[TreeNode, None]]:
        if not self.root:
            print("Tree is empty.")
            return
        else:
            if not parent:
                return self._search(self.root, key)
            else:
                return self._self_search_with_parent(None, self.root, key)

    def _search(self, node, key) -> Iterable[Union[TreeNode, None]]:
        if node is None:
            print("Key is not in the tree.")
            return None
        if node.data == key:
            print(f"Found {node.data}")
            return node, None
        if key < node.data:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def _self_search_with_parent(
        self, parent: TreeNode, node: TreeNode, key
    ) -> Iterable[Union[TreeNode, None]]:
        if not node:
            print("Key is not in the tree.")
            return None
        if node.data == key:
            print(f"Found {node.data}")
            return node, parent
        if key < node.data:
            return self._self_search_with_parent(node, node.left, key)
        else:
            return self._self_search_with_parent(node, node.right, key)

    def remove(self, key):
        if not self.root:
            print("Tree is empty")
            return None

        print("def remove(self, key):")
        item_node, parent_node = self.search(key, parent=True)
        if item_node is None:
            print("Item is not in the tree, can't be removed.")
            return
        else:
            self._remove(parent_node, item_node, key)

    def _remove(self, parent: TreeNode, node: TreeNode, key):
        ## Has no children, remove the node.
        if not node.left and not node.right:
            if node.data < parent.data:
                parent.left = None
            else:
                parent.right = None
        ## if has only one children. (XOR operator)
        elif (node.left and not node.right) or (not node.left and node.right):
            if node.left:
                if node.left.data < parent.data:
                    parent.left = node.left
                    return
                else:
                    parent.right = node.left
                    return
            if node.right:
                if node.right.data < parent.data:
                    parent.left = node.right
                    return
                else:
                    parent.right = node.right
                    return
        ## if node has two children, we replace min value of the right wing.
        ### min in always in the left side.
        elif node.left and node.right:
            # find the node with it's parent in node.right branch:
            temp_node = node.right
            temp_parent = node
            while temp_node.left:
                temp_parent = temp_node
                temp_node = temp_node.left
            node.data = temp_node.data
            self._remove(temp_parent, temp_node, temp_node.data)


if __name__ == "__main__":

    bt = BinaryTree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(15)
    bt.insert(2)
    bt.insert(7)
    bt.insert(12)
    bt.insert(20)

    print("Inorder Traversal: ", end="")
    bt.inorder(bt.root)  # Output: 2 5 7 10 12 15 20

    print("\nPreorder Traversal: ", end="")
    bt.preorder(bt.root)  # Output: 10 5 2 7 15 12 20

    print("\nPostorder Traversal: ", end="")
    bt.postorder(bt.root)  # Output: 2 7 5 12 20 15 10

    print("\nLevel Order Traversal: ", end="")
    bt.level_order()  # Output: 10 5 15 2 7 12 20

    print("\nLevel Order Traversal after remove: ", end="")
    # bt.remove(20)
    # bt.level_order()  # Output: 10 5 15 2 7 12 20

    bt.remove(10)
    bt.level_order()  # Output: 10 5 15 2 7 12 20

    ## sample b
    bt2 = BinaryTree()
    bt2.insert(5)
    bt2.insert(3)
    bt2.insert(7)
    bt2.insert(1)
    bt2.insert(13)
    bt2.insert(65)
    bt2.insert(0)
    bt2.insert(10)
    bt2.insert(63)
    bt2.insert(69)

    print("\nLevel Order Traversal after remove: ", end="")
    bt2.remove(13)
    bt2.level_order()
