# Project name : SPOJ: CSUMQ - Cumulative Sum Query
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-02
# Description  :
# Status       : Accepted (27641908)
# Tags         : python, doubly linked list, integer sequence A002262 (OEIS), card trick
# Comment      : It should not be accepted. This is O(n^2) solution.

from sys import stdin, stdout
from math import floor, sqrt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.no_of_elements = 0
    
    def __len__(self):
        return self.no_of_elements
    
    def append(self, data):
        new_node = Node(data)
        if self.no_of_elements:
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            new_node.next = self.head
        else:
            self.head.next = new_node
            self.head.prev = new_node
            new_node.prev = self.head
            new_node.next = self.head
        
        self.no_of_elements += 1
        
    def delete(self, n):
        k = 0
        node = self.head
        while k <= n:
            node = node.next
            k += 1
        
        node.next.prev = node.prev
        node.prev.next = node.next
        self.no_of_elements -= 1
        
        return node.data

def a(n):
    t = floor(sqrt(2*n + 1) + 0.5)
    return (t - t*t + 2*n)//2

def orderOfCards(no_of_cards):
    cards = [None for _ in range(no_of_cards)]
    k = 1
    i = 0
    while k + i < no_of_cards:
        cards[i + k] = k
        k += 1
        i += k
    
    remaining_cards = DoublyLinkedList()
    for i in range(no_of_cards):
        if cards[i] is None:
            remaining_cards.append(i)
        
    offset = no_of_cards - k + 1 - a(no_of_cards + 1)
    while k <= no_of_cards:
        offset = (offset + k) % len(remaining_cards)
        idx = remaining_cards.delete(offset)
        cards[idx] = k
        k += 1
    
    return cards

no_of_tests = int(stdin.readline())

for _ in range(no_of_tests):
    no_of_cards = int(stdin.readline())
    cards = orderOfCards(no_of_cards) 
    
    stdout.write('{}\n'.format(' '.join(map(str, cards))))

