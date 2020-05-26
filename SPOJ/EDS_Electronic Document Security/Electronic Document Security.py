# Project name : SPOJ: EDS - Electronic Document Security
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmial.com
# Date created : 2019-03-07
# Description  :
# Status       : Accepted (23362654)
# Tags         : python
# Comment      :

def currentACL(log):
    ACL = {}
    for entry in log.split(','):
        if '=' in entry:
            companies, rights = entry.split('=')
            rights = set(rights)
            for c in companies:
                ACL[c] = rights
        elif '+' in entry:
            companies, rights = entry.split('+')
            rights = set(rights)
            for c in companies:
                if c in ACL:
                    ACL[c] = ACL[c].union(rights)
                else:
                    ACL[c] = rights
        elif '-' in entry:
          companies, rights = entry.split('-')
          rights = set(rights)
          for c in companies:
              if c in ACL:
                  ACL[c] = ACL[c].difference(rights)
    return ACL

def printACL(ACL):
    ACL = list(filter(lambda x: x[1] != '', sorted(map(lambda x: (x[0], ''.join(sorted(x[1]))), ACL.items()), key=lambda x: x[0])))
    if len(ACL) > 0:
        print(ACL[0][0], end='')
        for i in range(1, len(ACL)):
            if ACL[i][1] == ACL[i - 1][1]:
                print(ACL[i][0], end='')
            else:
                print(ACL[i - 1][1] + ACL[i][0], end='')
        print(ACL[-1][1])
    else:
        print()

t = 1
while True:
    log = input()
    if log.strip() == '#':
        break
    ACL = currentACL(log)
    print(str(t) + ':', end='')
    printACL(ACL)
    t += 1
