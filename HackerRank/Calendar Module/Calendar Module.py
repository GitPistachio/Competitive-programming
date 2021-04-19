# Project name : HackerRank: Calendar Module
# Link         : https://www.hackerrank.com/challenges/calendar-module/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-17
# Description  :
# Status       : Accepted (209230395)
# Tags         : python
# Comment      : 

import calendar

calendar.setfirstweekday(calendar.MONDAY)

month, day, year = map(int, input().split())

print(list(calendar.day_name)[calendar.weekday(year, month, day)].upper())
