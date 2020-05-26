# Project name : SPOJ: AGPREFX - Agent prefix
# Author       : Wojciech Raszka
# Date created : 2019-03-29
# Description  :
# Status       : Accepted (23523093)
# Tags         : python
# Comment      :

agency_name = raw_input()
idx = int(raw_input())
msg = raw_input()

cyphred_msg = msg[:idx] + 'LUISS' + msg[idx + len(agency_name):]

print(cyphred_msg)
