# Project name : SPOJ: PPATH - Prime Path
# Link         : https://www.spoj.com/problems/PPATH/
# Try it on    : https://ideone.com/DplhqG
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-01
# Description  :
# Status       : Accepted (26078892)
# Tags         : python, indirected simple graph, binary search, prime numbers, queue, sieve of eratosthenes, breadth first search, BFS
# Comment      :

from queue import SimpleQueue
from sys import stdin, stdout

def getPrimes(a, b=None):
    if b is None:
        b = a
        a = 2
    
    if b < 2 or b < a:
        return []
    
    if a <= 2 and b >= 2:
        primes = [2]
    else:
        primes = []

    max_idx = b >> 1
    is_prime = [True for _ in range(max_idx + 1)]
    
    for i in range(3, b + 1, 2):
        idx = (i - 1) >> 1
        if is_prime[idx]:
            if i >= a:
                primes.append(i)
            step = (idx << 1) + 1
            idx += step
            while idx <= max_idx:
                is_prime[idx] = False
                idx += step
                
    
    return primes


def binarySearch(key, left, right, A):
    while left <= right:
        mid = left + (right - left)//2;
        
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

class Node:
    def __init__(self, id, data=None):
        self.id = id
        self.data = data
        self.outneighbours = set()
        self.inneighbours = set()
        self._outdegree = 0
        self._indegree = 0

    def addOutneighbour(self, nid):
        if nid not in self.outneighbours:
            self.outneighbours.add(nid)
            self._outdegree += 1

    def addInneighbour(self, nid):
        if nid not in self.inneighbours:
            self.inneighbours.add(nid)
            self._indegree += 1
    
    def outdegree(self):
        return self._outdegree

    def indegree(self):
        return self._indegree


class DirectedSimpleGraph:
    def __init__(self, order=0, data=None):
        self._size = 0
        if data is not None:
            self._order = len(data)
            self._nodes = [Node(id, x) for id, x in enumerate(data)]
        else:
            self._order = order
            self._nodes = [Node(id) for id in range(order)]
    
    def order(self):
        return self._order
    
    def size(self):
        return self._size
        
    def addEdge(self, nid1, nid2):
        self._nodes[nid1].addOutneighbour(nid2)
        self._nodes[nid2].addInneighbour(nid1)
        self._size += 1
    
    def shortestPath(self, nid1, nid2):
        if nid1 == nid2:
            return [nid1]

        Q = SimpleQueue()
        P = [-1 for _ in range(self.order())]
        visited = [False for _ in range(self.order())]
        Q.put(nid1)
        visited[nid1] = True
        
        while not Q.empty():
            nid = Q.get()
            
            for next_nid in self._nodes[nid].outneighbours:
                if not visited[next_nid]:
                    if next_nid == nid2:
                        path = [next_nid]
                        while nid > -1:
                            path.append(nid)
                            nid = P[nid]
                        return path
                            
                    P[next_nid] = nid
                    Q.put(next_nid)
                    visited[next_nid] = True

        return None
                

class UndirectedSimpleGraph(DirectedSimpleGraph):
    def __init__(self, order=0, data=None):
        super().__init__(order, data)

    def size(self):
        return super().size() >> 1

    def addEdge(self, nid1, nid2):
        super().addEdge(nid1, nid2)
        super().addEdge(nid2, nid1)



primes = getPrimes(1000, 9999)
no_of_primes = len(primes)
usg = UndirectedSimpleGraph(data=primes)

for nid1 in range(no_of_primes):
    p = primes[nid1]
    for r in range(4):
        factor = 10**r
        offset = ((p // factor) % 10)*factor
        for d in range(10):
            pp = p - offset + d*factor
            nid2 = binarySearch(pp, 0, no_of_primes - 1, primes)
            if nid2 != -1 and nid1 != nid2:
                usg.addEdge(nid1, nid2)


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    nid1, nid2 = map(lambda x: binarySearch(int(x), 0, no_of_primes - 1, primes), stdin.readline().split())
    path = usg.shortestPath(nid1, nid2)
    if path is not None:
        stdout.write("{}\n".format(len(path) - 1))
    else:
        stdout.write("Impossible\n")

