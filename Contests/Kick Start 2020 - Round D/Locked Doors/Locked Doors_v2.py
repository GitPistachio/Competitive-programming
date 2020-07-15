# Project name : Google: Kick Start 2020 - Round D: Locked Doors
# Link         : https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386d5c
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-15
# Description  :
# Status       : Accepted
# Tags         : python, all nearest smaller values, cartesian tree, binary lifting technique, DFS, depth first search, number of nodes in all subtrees, grapth theory, smallest power of 2 greater than or equal to n
# Comment      :

from sys import stdin, stdout
from collections import deque


def nearestNonSmaller(arr):
    n = len(arr)
    
    left_right = [[0, 0]]*n
    stack = deque()
    
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            j = stack.pop()
            if stack:
                left_right[j] = (stack[-1], i)
            else:
                left_right[j] = (-1, i)
                break

        stack.append(i)
    
    while stack:
        j = stack.pop()
        if stack:
            left_right[j] = (stack[-1], -1)
        else:
            left_right[j] = (-1, -1)
            break
    
    return left_right
    
def noOfNodes(n, adjacency_list, vid, parent, relevant_j):
    pending_nodes = [None]*n
    pending_nodes[0] = vid
    visited = [False]*n
    
    size = [1]*n
    i = 0
    cnt = 0
    while i >= 0:
        vid = pending_nodes[i]
        
        if visited[vid]:
            size[vid] = cnt - size[vid]
            i -= 1
        else:
            j = 0
            while parent[vid][j] != -1:
                parent[vid][j + 1] = parent[parent[vid][j]][j]
                j += 1
            relevant_j[vid] = j
 
            size[vid] = cnt
            cnt += 1
            visited[vid] = True
            for vnid in adjacency_list[vid]:
                i += 1
                pending_nodes[i] = vnid
    
    return size
    

def getLeft(adjacency_list, vid):
    if not adjacency_list[vid]:
        return None

    if len(adjacency_list[vid]) == 1:
        if adjacency_list[vid][0] < vid:
            return adjacency_list[vid][0]
        
        return None
    
    return min(adjacency_list[vid])

def getRight(adjacency_list, vid):
    if not adjacency_list[vid]:
        return None

    if len(adjacency_list[vid]) == 1:
        if adjacency_list[vid][0] > vid:
            return adjacency_list[vid][0]
        
        return None
    
    return max(adjacency_list[vid])

def findAncestor(parent, size, k, vid, j):
    while j >= 0:
        vmid = parent[vid][j]
    
        if vmid != -1 and size[vmid] < k:
            vid = vmid
        
        j -= 1
    
    if size[vid] >= k:
        return vid
    else:
        return parent[vid][0]

def c(n):
    cnt = 0
    while n > 0:
        n >>= 1
        cnt += 1
    return cnt

no_of_test_cases = int(stdin.readline())

for t in range(1, no_of_test_cases + 1):
    no_of_rooms, no_of_queries = map(int, stdin.readline().split())
    
    doors = list(map(int, stdin.readline().split()))
    no_of_doors = len(doors)
    
    intrestingLeftRight = nearestNonSmaller(doors)
    
    cartesian_tree = [-1]*no_of_doors
    for i in range(no_of_doors):
        left, right = intrestingLeftRight[i]
        if left >= 0:
            if right >= 0:
                if doors[left] < doors[right]:
                    cartesian_tree[i] = left
                else:
                    cartesian_tree[i] = right
            else:
                cartesian_tree[i] = left
        else:
            cartesian_tree[i] = right
            
            
    adjacency_list = [[] for _ in range(no_of_doors)]
    
    m = c(no_of_doors)
    parent = [[-1]*(m + 1) for _ in range(no_of_doors)]
    vrid = None

    for i in range(no_of_doors):
        if cartesian_tree[i] != -1:
            adjacency_list[cartesian_tree[i]].append(i)
            parent[i][0] = cartesian_tree[i]
        else:
            vrid = i

    relevant_j = [m]*no_of_doors
    size = noOfNodes(no_of_doors, adjacency_list, vrid, parent, relevant_j)
    
    ans = []
    for _ in range(no_of_queries):
        s, k = map(lambda x: int(x) - 1, stdin.readline().split())

        if s == 0:
            x = 0
        elif s == no_of_rooms - 1:
            x = no_of_doors - 1
        else:
            if doors[s - 1] < doors[s]:
                x = s - 1
            else:
                x = s

        if  size[x] >= k:
            if x < s:
                ans.append(s - k + 1)
            else:
                ans.append(s + k + 1)
        else:
            y = findAncestor(parent, size, k, x, relevant_j[x])
            if x < y:
                left_ynid = getLeft(adjacency_list, y)
                ans.append(y + k - size[left_ynid] + 1)
            else:
                right_ynid = getRight(adjacency_list, y)
                ans.append(y + 1 - (k - size[right_ynid]) + 1)

    
    
    stdout.write('Case #' + str(t) + ': ' + ' '.join(map(str, ans)) + '\n')
    