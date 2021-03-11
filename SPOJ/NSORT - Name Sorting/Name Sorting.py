# Project name : SPOJ: NSORT - Name Sorting
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-03-11
# Description  :
# Status       : Accepted (27541863)
# Tags         : python, math, roman numerals, arabic numerals, regnal number
# Comment      :

from sys import stdin, stdout

def romanToArabic(roman):
    '''Converts number in roman numeral system to number in arabic numeral system.'''
    symbolsValues = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    last_value = 0
    arabic = 0
    for symbol in roman[::-1]:
        value = symbolsValues[symbol]
        if value >= last_value:
            arabic += value
        else:
            arabic -= value
        
        last_value = value
	
    return arabic
    
def arabicToRoman(arabic):
    '''Converts number in arabic numeral system to number in roman numeral system.'''
    sortedRomanNumerals = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
    roman = ''
    k = 0
    while arabic > 0:
        while sortedRomanNumerals[k][1] > arabic:
            k += 1
        
        roman += sortedRomanNumerals[k][0]
        arabic -= sortedRomanNumerals[k][1]
    
    return roman
    
no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    no_of_kings = int(stdin.readline())
    kings = []
    for _ in range(no_of_kings):
        first_name, regnal_number = stdin.readline().strip().split()
        kings.append((first_name, romanToArabic(regnal_number)))
    
    kings.sort()
    for i in range(no_of_kings):
        stdout.write('{} {}\n'.format(kings[i][0], arabicToRoman(kings[i][1])))