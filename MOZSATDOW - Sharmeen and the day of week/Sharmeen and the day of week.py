# Project name : SPOJ: MOZSATDOW - Sharmeen and the day of week
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-11-13
# Description  :
# Status       : Accepted (24854150)
# Tags         : python
# Comment      :

days = {0 : 'Friday', 1 : 'Saturday', 2 : 'Sunday', 3 : 'Monday', 4 : 'Tuesday', 5 : 'Wednesday', 6 : 'Thursday'}

n = int(stdin.readline())

stdout.write('%s\n' % days[n % 7])
