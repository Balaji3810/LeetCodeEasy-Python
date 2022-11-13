# Definition for a binary tree node.
from typing import List
import collections
import json

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        q = collections.deque([root])
        
        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()

                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
s = Solution()
print(s.rightSideView(fromlist([1,2,3,None,5,None,4])))
