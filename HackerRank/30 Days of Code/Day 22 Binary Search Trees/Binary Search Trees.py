# Project name : HackerRank: Day 22: Binary Search Trees
# Link         : https://www.hackerrank.com/challenges/30-binary-search-trees/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-10
# Description  :
# Status       : Accepted (168244433)
# Tags         : python, binary search tree
# Comment      : 

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

    def getHeight(self, root):
        if not root:
            return -1
        
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       