# Project name : SPOJ: OFORTUNE - Ohgas' Fortune
# Author       : Wojciech Raszka
# Date created : 2019-03-20
# Description  :
# Status       : Accepted (23456788)
# Comment      :

def calculateFinalAmount(type_of_interest, initial_amount, no_of_years, annual_charge, interest_rate):
    amount = initial_amount

    if type_of_interest == '0':
        accumulated_interest = 0
        while no_of_years > 0:
            accumulated_interest += int(amount*interest_rate)
            amount -= annual_charge
            no_of_years -= 1
        amount += accumulated_interest
    else:
        while no_of_years > 0:
            amount += int(amount*interest_rate) - annual_charge
            no_of_years -= 1

    return amount

m = int(input())

while m > 0:
    initial_amount = int(input())
    no_of_years = int(input())
    n = int(input())

    max_balance = initial_amount
    while n > 0:
        tokens = input().split()
        type_of_operation = tokens[0]
        interest_rate = float(tokens[1])
        annual_charge = int(tokens[2])

        final_amount = calculateFinalAmount(type_of_operation, initial_amount, no_of_years, annual_charge, interest_rate)

        if max_balance < final_amount:
            max_balance = final_amount

        n -= 1
    print(max_balance)
    m -= 1
