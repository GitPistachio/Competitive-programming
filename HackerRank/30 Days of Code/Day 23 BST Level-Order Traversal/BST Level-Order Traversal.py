# Project name : HackerRank: Day 23: BST Level-Order Traversal
# Link         : https://www.hackerrank.com/challenges/30-binary-search-trees/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-11
# Description  :
# Status       : Accepted (168406194)
# Tags         : python, binary search tree, BST, level order traversal
# Comment      : 

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, root):
        from collections import deque

        nodes = deque()
        data = []
        if root:
            nodes.append(root)

            while nodes:
                node = nodes.popleft()
                data.append(node.data)
                
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
        print(' '.join(map(str, data)))


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
