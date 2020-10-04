# Project name : HackerRank: Fraudulent Activity Notifications
# Link         : https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-15
# Description  :
# Status       : Accepted (169643289)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    freq = [0]*201

    for e in expenditure[:d]:
        freq[e] += 1
    
    n = len(expenditure)
    dh = d//2
    isOdd = d & 1
    no_of_notifications = 0
    for i in range(d, n):
        cnt = 0
        # print(freq)
        for j in range(201):
            cnt += freq[j]
            if cnt >= dh:
                j += 1
                # print(' ', j - 1)
                break
        
        if isOdd:
            if cnt == dh:
                while freq[j] == 0:
                    j += 1
            
                median = j << 1
            else:
                median = (j - 1) << 1
        else:
            if cnt == dh:
                median = j - 1
                while freq[j] == 0:
                    j += 1
                median = (j + median)
            else:
                median = (j - 1) << 1

        le = expenditure[i - d]
        e = expenditure[i]
        freq[le] -= 1
        freq[e] += 1

        if e >= median:
            no_of_notifications += 1
        
        # print(i, e, median, no_of_notifications, d, isOdd, dh)
        
    return no_of_notifications

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
