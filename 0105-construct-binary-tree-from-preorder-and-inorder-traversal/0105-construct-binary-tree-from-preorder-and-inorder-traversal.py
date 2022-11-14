# Definition for a binary tree node.
from typing import List
from typing import Optional
import collections
import json

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
      return '[%s, %r, %r]' % (self.val, self.left, self.right)


def fromlist(values):
    def create(it):
        value = next(it)
        return None if value is None else TreeNode(value)
        
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    nextlevel = [root]
    try:
        while nextlevel:
            level = nextlevel
            nextlevel = []
            for node in level:
                if node:
                    node.left = create(it)
                    node.right = create(it)
                    nextlevel += [node.left, node.right]
        
    except StopIteration:
        return root
    raise ValueError("Invalid list")
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid +1:], inorder[mid +1:])

        return root
      
s = Solution()
print(s.buildTree([3,9,20,15,7],[9,3,15,20,7]))
