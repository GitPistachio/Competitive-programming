# Project name : CodeChef: COVDSMPL - Covid Sampling (Challenge)
# Link         : https://www.codechef.com/JUNE20B/problems/COVDSMPL
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-06-08
# Description  :
# Status       : (???)
# Tags         : python
# Comment      : 

from sys import exit, stdin, stdout


def askQst(r1, c1, r2, c2, known_x=0):
    global n
    global total_cost
    global qsts
    qst = '1 ' + str(r1 + 1) + ' ' + str(c1 + 1) + ' ' + str(r2 + 1) + ' ' + str(c2 + 1) + '\n'
    if qst in qsts:
        return qsts[qst] - known_x
    stdout.write(qst)
    stdout.flush()
    x = int(stdin.readline())
    if x == -1:  # Asked to many questions
        exit()

    qsts[qst] = x
    total_cost += getCost(n, r1, c1, r2, c2, x)
    return x - known_x


def askQstOpt(n, total_infected, r1, c1, r2, c2, known_x=0):
    rows = r2 - r1 + 1
    cols = c2 - c1 + 1
    est_known_x = max(known_x, total_infected*rows*cols//(n*n))
    # print("s", n, no_of_people, r1, c1, r2, c2, known_x)
    if c1 == 0 and c2 < n - 1:
        extra_possible_x = total_infected*rows*(n - cols)//(n*n)  # it should be E[X|Y]
        extra_possible_x = min(total_infected - est_known_x, extra_possible_x)
        cost1_strategy = (r1, c2 + 1, r2, n - 1, extra_possible_x)
        cost2_strategy = (r1, 0, r2, n - 1, est_known_x + extra_possible_x)
    elif c2 == n - 1:
        extra_possible_x = total_infected*rows*(n - cols)//(n*n)  # it should be E[X|Y]
        extra_possible_x = min(total_infected - est_known_x, extra_possible_x)
        cost1_strategy = (r1, 0, r2, c1 - 1, extra_possible_x)
        cost2_strategy = (r1, 0, r2, n - 1, est_known_x + extra_possible_x)
    elif r1 == 0 and r2 < n - 1:
        extra_possible_x = total_infected*(n - rows)*cols//(n*n)  # it should be E[X|Y]
        extra_possible_x = min(total_infected - est_known_x, extra_possible_x)
        cost1_strategy = (r2 + 1, c1, n - 1, c2, extra_possible_x)
        cost2_strategy = (0, c1, n - 1, c2, est_known_x + extra_possible_x)
    else:
        return askQst(r1, c1, r2, c2, known_x)

    cost = getCost(n, r1, c1, r2, c2, est_known_x)
    cost1 = getCost(n, *cost1_strategy)
    cost2 = getCost(n, *cost2_strategy)

    if cost2_strategy[:4] == (0, 0, n - 1, n - 1) and cost1 < cost:
        cost1_x = askQst(*cost1_strategy[:4])
        return total_infected - cost1_x - known_x

    if cost1 + cost2 < cost:
        cost1_x = askQst(*cost1_strategy[:4])

        if cost1_x + known_x == total_infected:
            return 0

        cost2_x = askQst(*cost2_strategy[:4], known_x)

        return cost2_x - cost1_x
    else:
        return askQst(r1, c1, r2, c2, known_x)


def fillCovidMatrix(M, r1, c1, r2, c2, val):
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            M[i][j] = val


def noOfPeople(M, r1, c1, r2, c2):
    no_of_people = 0
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            if M[i][j] == '1':
                no_of_people += 1

    return no_of_people


def checkMaxExpand(M, r1, c1, r2, c2, grow_side):
    no_of_people = 0
    if grow_side == 'lower':
        for i in range(r1, r2 + 1):
            no_of_people_in_row_col = 0
            for j in range(c1, c2 + 1):
                if M[i][j] == '':
                    return (i - 1, no_of_people)
                elif M[i][j] == '1':
                    no_of_people_in_row_col += 1
            no_of_people += no_of_people_in_row_col

        return (r2, no_of_people)

    elif grow_side == 'right':
        for j in range(c1, c2 + 1):
            no_of_people_in_row_col = 0
            for i in range(r1, r2 + 1):
                if M[i][j] == '':
                    return (j - 1, no_of_people)
                elif M[i][j] == '1':
                    no_of_people_in_row_col += 1
            no_of_people += no_of_people_in_row_col

        return (c2, no_of_people)

    elif grow_side == 'upper':
        for i in range(r2, r1 - 1, -1):
            no_of_people_in_row_col = 0
            for j in range(c1, c2 + 1):
                if M[i][j] == '':
                    return (i + 1, no_of_people)
                elif M[i][j] == '1':
                    no_of_people_in_row_col += 1
            no_of_people += no_of_people_in_row_col

        return (r1, no_of_people)
    else:
        for j in range(c2, c1 - 1, -1):
            no_of_people_in_row_col = 0
            for i in range(r1, r2 + 1):
                if M[i][j] == '':
                    return (j + 1, no_of_people)
                elif M[i][j] == '1':
                    no_of_people_in_row_col += 1
            no_of_people += no_of_people_in_row_col

        return (c1, no_of_people)


def getCost(n, r1, c1, r2, c2, x):
    rows = r2 - r1 + 1
    cols = c2 - c1 + 1
    return (2*n - rows)*(2*n - cols)/(1 + x)


def findMinMaxCost(M, n, r1, c1, r2, c2, blocked_side):
    if blocked_side == 'lower':
        max_left, x_left = checkMaxExpand(M, r1, 0, r2, c1 - 1, 'left')
        max_right, x_right = checkMaxExpand(M, r1, c2 + 1, r2, n - 1, 'right')
        x = x_left + x_right
        min_max_strategy = (r1, max_left, r2, max_right, x)
        min_max_cost = getCost(n, *min_max_strategy)
        for r in range(r1 - 1, -1, -1):
            right, x_right = checkMaxExpand(M, r, c1, r, max_right, 'right')
            if right < c2:
                break
            x += x_right - noOfPeople(M, r + 1, right + 1, r2, max_right)
            max_right = right

            if max_left < c1:
                left, x_left = checkMaxExpand(M, r, max_left, r, c1 - 1, 'left')
                x += x_left - noOfPeople(M, r + 1, max_left, r2, left - 1)
                max_left = left

            strategy = (r, max_left, r2, max_right, x)
            cost = getCost(n, *strategy)
            if cost < min_max_cost:
                min_max_cost = cost
                min_max_strategy = strategy
    elif blocked_side == 'upper':
        max_left, x_left = checkMaxExpand(M, r1, 0, r2, c1 - 1, 'left')
        max_right, x_right = checkMaxExpand(M, r1, c2 + 1, r2, n - 1, 'right')
        x = x_left + x_right
        min_max_strategy = (r1, max_left, r2, max_right, x)
        min_max_cost = getCost(n, *min_max_strategy)
        for r in range(r2 + 1, n):
            right, x_right = checkMaxExpand(M, r, c1, r, max_right, 'right')
            if right < c2:
                break
            x += x_right - noOfPeople(M, r1, right + 1, r - 1, max_right)
            max_right = right

            if max_left < c1:
                left, x_left = checkMaxExpand(M, r, max_left, r, c1 - 1, 'left')
                x += x_left - noOfPeople(M, r1, max_left, r - 1, left - 1)
                max_left = left

            strategy = (r1, max_left, r, max_right, x)
            cost = getCost(n, *strategy)
            if cost < min_max_cost:
                min_max_cost = cost
                min_max_strategy = strategy
    elif blocked_side == 'left':
        max_upper, x_upper = checkMaxExpand(M, 0, c1, r1 - 1, c2, 'upper')
        max_lower, x_lower = checkMaxExpand(M, r2 + 1, c1, n - 1, c2, 'lower')
        x = x_upper + x_lower
        min_max_strategy = (max_upper, c1, max_lower, c2, x)
        min_max_cost = getCost(n, *min_max_strategy)
        for c in range(c2 + 1, n):
            lower, x_lower = checkMaxExpand(M, r1, c, max_lower, c, 'lower')
            if lower < r2:
                break
            x += x_lower - noOfPeople(M, lower + 1, c1, max_lower, c - 1)
            max_lower = lower

            if max_upper < r1:
                upper, x_upper = checkMaxExpand(M, max_upper, c, r1 - 1, c, 'upper')
                x += x_upper - noOfPeople(M, max_upper, c1, upper - 1, c - 1)
                max_upper = upper

            strategy = (max_upper, c1, max_lower, c, x)
            cost = getCost(n, *strategy)
            if cost < min_max_cost:
                min_max_cost = cost
                min_max_strategy = strategy
    else:
        max_upper, x_upper = checkMaxExpand(M, 0, c1, r1 - 1, c2, 'upper')
        max_lower, x_lower = checkMaxExpand(M, r2 + 1, c1, n - 1, c2, 'lower')
        x = x_upper + x_lower
        min_max_strategy = (max_upper, c1, max_lower, c2, x)
        min_max_cost = getCost(n, *min_max_strategy)
        for c in range(c1 - 1, -1, -1):
            lower, x_lower = checkMaxExpand(M, r1, c, max_lower, c, 'lower')
            if lower < r2:
                break
            x += x_lower - noOfPeople(M, lower + 1, c + 1, max_lower, c2)
            max_lower = lower

            if max_upper < r1:
                upper, x_upper = checkMaxExpand(M, max_upper, c, r1 - 1, c, 'upper')
                x += x_upper - noOfPeople(M, max_upper, c + 1, upper - 1, c2)
                max_upper = upper

            strategy = (max_upper, c, max_lower, c2, x)
            cost = getCost(n, *strategy)
            if cost < min_max_cost:
                min_max_cost = cost
                min_max_strategy = strategy

    return (min_max_cost, min_max_strategy)


def solveByRow(M, n, r1, c1, r2, c2, mid_r, lower_min_max_cost, upper_min_max_cost, no_of_missing_ones, total_infected):
    if upper_min_max_cost[0] < lower_min_max_cost[0]:
        # x = askQst(*upper_min_max_cost[1])
        x = askQstOpt(n, total_infected, *upper_min_max_cost[1])
        solve(M, n, mid_r + 1, c1, r2, c2, x, total_infected)
        solve(M, n, r1, c1, mid_r, c2, no_of_missing_ones - x, total_infected)
    else:
        # x = askQst(*lower_min_max_cost[1])
        x = askQstOpt(n, total_infected, *lower_min_max_cost[1])
        solve(M, n, r1, c1, mid_r, c2, x, total_infected)
        solve(M, n, mid_r + 1, c1, r2, c2, no_of_missing_ones - x, total_infected)


def solveByCol(M, n, r1, c1, r2, c2, mid_c, left_min_max_cost, right_min_max_cost, no_of_missing_ones, total_infected):
    if left_min_max_cost[0] < right_min_max_cost[0]:
        # x = askQst(*left_min_max_cost[1])
        x = askQstOpt(n, total_infected, *left_min_max_cost[1])
        solve(M, n, r1, mid_c + 1, r2, c2, x), total_infected
        solve(M, n, r1, c1, r2, mid_c, no_of_missing_ones - x, total_infected)
    else:
        # x = askQst(*right_min_max_cost[1])
        x = askQstOpt(n, total_infected, *right_min_max_cost[1])
        solve(M, n, r1, c1, r2, mid_c, x, total_infected)
        solve(M, n, r1, mid_c + 1, r2, c2, no_of_missing_ones - x, total_infected)


def solve(M, n, r1, c1, r2, c2, no_of_missing_ones, total_infected):
    if no_of_missing_ones == 0:
        fillCovidMatrix(M, r1, c1, r2, c2, '0')
        return

    no_of_people = (r2 - r1 + 1)*(c2 - c1 + 1)
    if no_of_missing_ones == no_of_people:
        fillCovidMatrix(M, r1, c1, r2, c2, '1')
        return

    # by row cost
    if r2 > r1:
        if c2 > c1:
            mid_r = r1 + (r2 - r1)//2
            upper_min_max_cost = findMinMaxCost(M, n, mid_r + 1, c1, r2, c2, 'upper')
            lower_min_max_cost = findMinMaxCost(M, n, r1, c1, mid_r, c2, 'lower')

            mid_c = c1 + (c2 - c1)//2
            right_min_max_cost = findMinMaxCost(M, n, r1, c1, r2, mid_c, 'right')
            left_min_max_cost = findMinMaxCost(M, n, r1, mid_c + 1, r2, c2, 'left')

            if min(lower_min_max_cost[0], upper_min_max_cost[0]) < min(left_min_max_cost[0], right_min_max_cost[0]):
                solveByRow(M, n, r1, c1, r2, c2, mid_r, lower_min_max_cost, upper_min_max_cost, no_of_missing_ones, total_infected)
            else:
                solveByCol(M, n, r1, c1, r2, c2, mid_c, left_min_max_cost, right_min_max_cost, no_of_missing_ones, total_infected)
        else:
            mid_r = r1 + (r2 - r1)//2
            upper_min_max_cost = findMinMaxCost(M, n, mid_r + 1, c1, r2, c2, 'upper')
            lower_min_max_cost = findMinMaxCost(M, n, r1, c1, mid_r, c2, 'lower')

            solveByRow(M, n, r1, c1, r2, c2, mid_r, lower_min_max_cost, upper_min_max_cost, no_of_missing_ones, total_infected)
    else:
        mid_c = c1 + (c2 - c1)//2
        right_min_max_cost = findMinMaxCost(M, n, r1, c1, r2, mid_c, 'right')
        left_min_max_cost = findMinMaxCost(M, n, r1, mid_c + 1, r2, c2, 'left')

        solveByCol(M, n, r1, c1, r2, c2, mid_c, left_min_max_cost, right_min_max_cost, no_of_missing_ones, total_infected)


def guessCovidMatrix(n, p):
    if p == 0:
        return [['0']*n]*n
    elif p == 100:
        return [['1']*n]*n

    x = askQst(0, 0, n - 1, n - 1)

    M = [['']*n for _ in range(n)]
    solve(M, n, 0, 0, n - 1, n - 1, x, x)

    return M


def printCovidMatrix(M):
    for row in M:
        stdout.write(' '.join(row) + '\n')
    stdout.flush()


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    n, p = map(int, stdin.readline().split())
    total_cost = 0
    qsts = {}
    M = guessCovidMatrix(n, p)
    #print(total_cost)

    stdout.write("2\n")
    printCovidMatrix(M)

    x = int(stdin.readline())
    if x == -1:
        exit()
