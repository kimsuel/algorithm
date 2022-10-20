"""
- 문제
Given the roots of two binary trees p and q,
write a function to check if they are the same or not.

Two binary trees are considered the same 
if they are structurally identical, and the nodes have the same value.

- 예시
Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))


p = [1, 2]
q = [1, None, 2]

p_root = TreeNode(1, TreeNode(2))
q_root = TreeNode(1, None, TreeNode(2))

solution = Solution()
print(solution.isSameTree(p_root, q_root))
