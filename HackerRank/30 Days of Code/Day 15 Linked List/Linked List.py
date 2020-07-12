# Project name : HackerRank: Day 15: Linked List
# Link         : https://www.hackerrank.com/challenges/30-linked-list/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-03
# Description  :
# Status       : Accepted (167018361)
# Tags         : python, linked list
# Comment      : 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self, head, data): 
        new_node = Node(data)
        if head is None:
            head = new_node
        
        else:
            node = head
            while node.next is not None:
                node = node.next
            
            node.next = new_node
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head)
