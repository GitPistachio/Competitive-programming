#There is something wrong with the input
n = int(input())
while n != 0:
    month_sales = [0]*n
    while n > 0:
        r = list(map(int, input().split(' ')))
        for i in range(len(month_sales)):
            month_sales[i] += r[i]
        n -= 1
    print(','.join(map(str, month_sales)))
    n = int(input())
