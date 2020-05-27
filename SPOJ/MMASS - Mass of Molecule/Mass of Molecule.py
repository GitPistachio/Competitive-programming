# Project name : SPOJ: MMASS - Mass of Molecule
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-21
# Description  :
# Status       : Accepted (23544204)
# Tags         : python, chemistry, execuction of expression
# Comment      :

class stack():
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)

    def last(self):
        return self.data[-1]

    def pop(self):
        if self.isEmpty():
            return None

        return self.data.pop()

    def __str__(self):
        return str(self.data)


molecules = {'H':1, 'O':16, 'C':12}
formula = input().strip().split()[0]

mass = stack()
for e in formula:
    if e in '0123456789':
        m = mass.pop()
        if m in molecules:
            mass.push(molecules[m]*int(e))
        else:
            mass.push(m*int(e))

    elif e in ')':
        m = 0
        s = mass.pop()
        while True:
            if s in molecules:
                m += molecules[s]
            elif type(s) is int:
                m += s
            else:
                break
            s = mass.pop()
        mass.push(m)
    else:
        mass.push(e)

m = 0
s = mass.pop()
while True:
    if s in molecules:
        m += molecules[s]
    elif type(s) is int:
        m += s
    else:
        break

    s = mass.pop()
mass.push(m)

print(mass.pop())
