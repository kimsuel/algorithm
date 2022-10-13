# 104
# maximum depth of binary tree

"""
- 문제.
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input : root = [3,9,20,null,null,15,7]
Output : 3

Input : root = [1,null,2]
Output : 2
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        max_depth = []

        def dfs(node, depth):
            if not node:
                max_depth.append(depth)
                return

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0)
        return max(max_depth)


root = [3, 9, 20, None, None, 15, 7]
node1 = TreeNode(20, TreeNode(15), TreeNode(7))
node2 = TreeNode(9, None, None)
root = TreeNode(3, node2, node1)

solution = Solution()
print(solution.maxDepth(root))
