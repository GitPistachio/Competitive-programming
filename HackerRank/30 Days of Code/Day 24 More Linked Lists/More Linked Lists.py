# Project name : HackerRank: Day 24: More Linked Lists
# Link         : https://www.hackerrank.com/challenges/30-linked-list-deletion/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-12
# Description  :
# Status       : Accepted (168472269)
# Tags         : python, linked list
# Comment      : 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self, head):
        last_node = head
        node = head.next
        while node:
            if node.data != last_node.data:
                last_node.next = node
                last_node = node
            
            node = node.next
        
        last_node.next = None
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 