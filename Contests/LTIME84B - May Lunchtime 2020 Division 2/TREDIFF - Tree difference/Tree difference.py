# Project name : CodeChef: TREDIFF - Tree difference
# Link         : https://www.codechef.com/LTIME84B/problems/TREDIFF
# Try it on    : https://ideone.com/aiDG3c
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-02
# Description  :
# Status       : Accepted(33557948)
# Tags         : python, graph, tree graph, frequency table, min difference between elements, bfs, breadth first search, pigeonhole principle
# Comment      : 100

from sys import stdin, stdout


class DirectedSimpleGraph:
    def __init__(self, order=0, data=None):
        self._size = 0
        if data is not None:
            self._data = data
            self._order = len(self._data)
            self._nodes = [[] for _ in range(self._order)]
        else:
            self._order = order
            self._data = [None]*self._order
        
        self._parent_nodes = [-1]*self._order
        self._depth = [-1]*self._order
    
    def order(self):
        return self._order
    
    def size(self):
        return self._size
        
    def addEdge(self, nid1, nid2):
        self._nodes[nid1].append(nid2)
        self._size += 1
    
    def bfs(self):
        nodes_queue = [0]*self._order
        pos = 0
        self._depth[0] = 0
        while pos >= 0:
            nid = nodes_queue[pos]
            pos -= 1
            depth = self._depth[nid] + 1
            for next_nid in self._nodes[nid]:
                if self._depth[next_nid] == -1:
                    self._depth[next_nid] = depth
                    self._parent_nodes[next_nid] = nid
                    pos += 1
                    nodes_queue[pos] = next_nid
    
    def solve(self, nid1, nid2, max_a):
        if self._depth[nid1] < self._depth[nid2]:
            nid1, nid2 = nid2, nid1
        
        occurence_tab = [False]*(max_a + 1)
        while self._depth[nid1] != self._depth[nid2]:
            a = self._data[nid1]
            if occurence_tab[a]:
                return 0
            occurence_tab[a] = True
            nid1 = self._parent_nodes[nid1]
        
        while nid1 != nid2:
            a = self._data[nid1]
            if occurence_tab[a]:
                return 0
            occurence_tab[a] = True
            b = self._data[nid2]
            if occurence_tab[b]:
                return 0
            occurence_tab[b] = True
            nid1, nid2 = self._parent_nodes[nid1], self._parent_nodes[nid2]
        
        a = self._data[nid1]
        if occurence_tab[a]:
                return 0
        occurence_tab[a] = True
        
        i = 0
        while i <= max_a:
            if occurence_tab[i]:
                min_a = i
                break
            i += 1
        
        d = max_a
        prev_a = min_a
        i += 1
        while i <= max_a:
            if occurence_tab[i]:
                if i - prev_a < d:
                    d = i - prev_a
                
                prev_a = i
            i += 1
        
        return d


class UndirectedSimpleGraph(DirectedSimpleGraph):
    def __init__(self, order=0, data=None):
        super().__init__(order, data)

    def size(self):
        return super().size() >> 1

    def addEdge(self, nid1, nid2):
        super().addEdge(nid1, nid2)
        super().addEdge(nid2, nid1)


no_of_test_cases = int(stdin.readline())

for _ in range(no_of_test_cases):
    n, q = map(int, stdin.readline().split())
    data = map(int, stdin.readline().split())
    usg = UndirectedSimpleGraph(data=list(data))
    for _ in range(n - 1):
        nid1, nid2 = map(lambda x: int(x) - 1, stdin.readline().split())
        usg.addEdge(nid1, nid2)
    
    usg.bfs()
    for _ in range(q):
        nid1, nid2 = map(lambda x: int(x) - 1, stdin.readline().split())
        d = usg.solve(nid1, nid2, 100)
        stdout.write(str(d) + "\n")
            
