# Project name : SPOJ: CLOCK2 - The Famous Clock
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-03-11
# Description  :
# Status       : Accepted (27541974)
# Tags         : python, math, roman numerals, arabic numerals
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

t = 1
for line in stdin:
	roman_numeral = line.strip()
	arabic_numeral = romanToArabic(roman_numeral)
	stdout.write("Case {}: {}\n".format(t, arabic_numeral))
	t += 1