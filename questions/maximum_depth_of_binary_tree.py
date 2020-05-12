# Definition for a binary tree node.
import TreeNode
import unittest
from collections import deque

def maxDepth(root: TreeNode) -> int:
    """https://leetcode.com/problems/maximum-depth-of-binary-tree/
    """
    
    # Using dequeue
    queue = deque([(root, 1)]) # Deque initialization reads tuples 1 at a time under the hood, same for lists
    # Get around this by wrapping whatever you put in to stop unpacking
    max_dist = 0
    while queue:
        node, distance = queue.popleft()
        if node == None:
            continue
        max_dist = max(max_dist, distance)
        queue.append((node.left, distance + 1))
        queue.append((node.right, distance + 1))
    return max_dist
    
    # Using array
    # queue = []
    # if root == None:
    #     return 0
    # queue.append((root, 1))
    # for pair in queue:
    
    # Recursive    
    # if root == None: 
    #     return 0
    # return 1 + max(maxDepth(root.left), maxDepth(root.right))

class TestStringMethods(unittest.TestCase):
    def test_1(self):
        root = TreeNode.TreeNode()
        self.assertEqual(maxDepth(root), 1)
    def test_2(self):
        root = TreeNode.TreeNode()
        root.left = TreeNode.TreeNode()
        self.assertEqual(maxDepth(root), 2)
if __name__ == "__main__":
    unittest.main()
