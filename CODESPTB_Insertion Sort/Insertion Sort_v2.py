# Merge Sort
#Time complexity O(nlogn)
def merge(A, p, q, r):
    i = p
    k = 0
    j = q
    inv_count = 0
    T = [0]*(r - p + 1)

    while i <= q - 1 and j <= r:
        if A[i] <= A[j]:
            T[k] = A[i]
            i += 1
        else:
            T[k] = A[j]
            j += 1
            inv_count += q - i
        k += 1

    if i <= q - 1:
        while i <= q - 1:
            T[k] = A[i]
            i += 1
            k += 1
    else:
        while j <= r:
            T[k] = A[j]
            j += 1
            k += 1

    for i in range(0, r - p + 1):
        A[p + i] = T[i]

    return inv_count

def mergeSort(A, p, r):
    inv_count = 0
    if p < r:
        q = (p + r)//2
        inv_count += mergeSort(A, p, q)
        inv_count += mergeSort(A, q + 1, r)
        inv_count += merge(A, p, q + 1, r)

    return inv_count

T = int(input())

for t in range(T):
    N = int(input())
    A = list(map(int, input().split(' ')))

    print(mergeSort(A, 0, N - 1))
