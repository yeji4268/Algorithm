def infix_to_postfix(exp):
    operator = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = list()
    res = list()
    
    for token in exp:
        if token.isalnum():
            res.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                res.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and operator[token] <= operator.get(stack[-1], 0):
                res.append(stack.pop())
            stack.append(token)
    
    while stack:
        res.append(stack.pop())
    return ''.join(res)

exp = input()
print(infix_to_postfix(exp))