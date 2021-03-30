# Project name : CodeChef: INPSTFIX - Infix to Postfix
# Link         : https://www.codechef.com/LRNDSA02/problems/INPSTFIX
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-20
# Description  :
# Status       : Accepted (34543964)
# Tags         : python, linear data structure, infix expression, postifx expression, rpn, reverse polish notation, Shunting-yard algorithm
# Comment      :


from sys import exit, stdin, stdout
from collections import deque

def tokenize(expr, alphabet, digits, decimal_sep, param_sep, operators, whitespaces, opening_bracket, closing_bracket):
    n = len(expr)
    i = 0
    token = ''
    token_type = None
    while i < n:
        symbol = expr[i]
        if symbol not in whitespaces:
            if token == '':
                if symbol in operators:
                    yield (symbol, 'operator')
                elif symbol in alphabet:
                    token = symbol
                    token_type = 'variable'
                elif symbol in digits:
                    token = symbol
                    token_type = 'number'
                elif symbol == opening_bracket or symbol == closing_bracket:
                    yield (symbol, 'bracket')
                else:
                    raise Exception('Unrecognized symbol')
            else:
                if symbol in operators or symbol == closing_bracket or symbol == param_sep:
                    yield (token, token_type)
                    if symbol == closing_bracket:
                        yield (symbol, 'bracket')
                    elif symbol == param_sep:
                        yield (symbol, 'parameter_separator')
                    else:
                        yield (symbol, 'operator')
                    token = ''
                elif symbol in alphabet and token_type != 'number':
                    token += symbol
                elif symbol in digits:
                    token += symbol
                elif symbol == decimal_sep:
                    token += symbol
                elif symbol == opening_bracket:
                    yield (token, 'function')
                    yield (symbol, 'bracket')
                    token = ''
                else:
                    raise Exception('Unrecognized symbol')
        i += 1
    
    if token != '':
        yield (token, token_type)
            
        

def infixToPostfix(infix_expr):
    alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    digits = set('0123456789')
    decimal_sep = '.'
    param_sep = ','
    operators = {'+': (2, 'left'), '-': (2, 'left'), '*': (3, 'left'), '/': (3, 'left'), '^': (4, 'left')}
    whitespaces = set([' ', '\n'])
    opening_bracket = '('
    closing_bracket = ')'
    tokens = tokenize(infix_expr, alphabet, digits, decimal_sep, param_sep, set(operators.keys()), whitespaces, opening_bracket, closing_bracket)
    
    postfix_expr = ''
    operator_stack = deque()
    for token,token_type in tokens:
        if token_type == 'variable' or token_type == 'number':
            postfix_expr += token
        elif token_type == 'function':
            operator_stack.append((token, token_type))
        elif token_type == 'operator':
            while operator_stack and operator_stack[-1][0] != opening_bracket:
                if not (operator_stack[-1][1] == 'function'
                        or (operator_stack[-1][1] == 'operator'
                            and (operators[token][0] < operators[operator_stack[-1][0]][0]
                                 or (operators[token][0] == operators[operator_stack[-1][0]][0] and operators[token][1] == 'left')
                                )
                           )
                       ):
                     break
                postfix_expr += operator_stack.pop()[0]

            operator_stack.append((token, token_type))
        elif token == opening_bracket:
            operator_stack.append((token, token_type))
        elif token == closing_bracket:
            while operator_stack and operator_stack[-1][0] != '(':
                postfix_expr += operator_stack.pop()[0]
            
            if not operator_stack:
                raise Exception('Expression is not well-bracked')
            
            operator_stack.pop()
        #print(token, postfix_expr, operator_stack)
    
    while operator_stack:
        if operator_stack[-1][0] == opening_bracket:
            raise Exception('Expression is not well-bracked')
        postfix_expr += operator_stack.pop()[0]
    
    return postfix_expr


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    n  = int(stdin.readline())
    infix_expr = stdin.readline().strip()
    postfix_expr = infixToPostfix(infix_expr)
    stdout.write(postfix_expr +'\n')