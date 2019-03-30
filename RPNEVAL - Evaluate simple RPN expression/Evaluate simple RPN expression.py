# Project name : SPOJ: RPNEVAL - Evaluate simple RPN expression
# Author       : Wojciech Raszka
# Date created : 2019-03-13
# Description  :
# Status       : Accepted (23402948)
# Comment      :

import sys

def evalRPN(rpn):
    stack = []
    for token in rpn.split():
        if len(stack) >= 2:
            if token == '+':
                try:
                    stack.append(stack.pop() + stack.pop())
                except:
                    raise Exception("Invalid rpn expression")
            elif token == '-':
                try:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                except:
                    raise Exception("Invalid rpn expression")
            elif token == '/':
                try:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b/a)
                except:
                    raise Exception("Invalid rpn expression")
            elif token == '*':
                try:
                    stack.append(stack.pop()*stack.pop())
                except:
                    raise Exception("Invalid rpn expression")
            else:
                try:
                    stack.append(float(token))
                except:
                    raise Exception("Invalid rpn expression")
        else:
            try:
                stack.append(float(token))
            except:
                raise Exception("Invalid rpn expression")

    if len(stack) == 1:
        return stack[0]
    else:
        raise Exception("Invalid rpn expression")

for rpn in sys.stdin:
    try:
        print("%.4f" % round(evalRPN(rpn), 4))
    except:
        print("ERROR")
