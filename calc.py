import operator
def convert(expr):
    answ = []
    stek = []
    u = []
    expr = expr.replace('(', '( ')
    expr = expr.replace(')', ' )')
    expr = expr.replace('-', ' - ')
    for i in expr.split():
        if i.isdigit():
            answ.append(i)
        elif i == '(':
            u.append(i)
        elif i in '+-':
            if u != []:
                if u[(len(u)) - 1] in '+-*//%^':
                    u.reverse()
                    answ.extend(u[:u.index('(')])
                    for j in u[:u.index('(')]:
                        u.remove(j)
                u.append(i)
            else:
                if stek != [] and stek[(len(stek)) - 1] in '+-*//%^':
                    answ.append(stek.pop((len(stek)) - 1))
                stek.append(i)
        elif i in '*//%':
            if u != []:
                if u[(len(u)) - 1] in '*//%^':
                    u.reverse()
                    answ.extend(u[:u.index('(')])
                    for j in u[:u.index('(')]:
                        u.remove(j)
                u.append(i)
            else:
                if stek != [] and stek[(len(stek)) - 1] in '*//%^':
                    answ.append(stek.pop((len(stek)) - 1))
                stek.append(i)
        elif i in '^':
            if u != []:
                if u[(len(u)) - 1] in '^':
                    u.reverse()
                    answ.extend(u[:u.index('(')])
                    for j in u[:u.index('(')]:
                        u.remove(j)
                u.append(i)
            else:
                if stek != [] and stek[(len(stek)) - 1] in '^':
                    answ.append(stek.pop((len(stek)) - 1))
                stek.append(i)
        elif i == ')':
            u.reverse()
            answ.extend(u[:u.index('(')])
            for j in u[:u.index('(')+1]:
                u.remove(j)
            u.reverse()
    stek.reverse()
    answ.extend(stek)
    return (' '.join(answ))

def calc(expr):
    expr = convert(expr)
    expr = expr.replace('^','**')
    OPERATORS = {
     '+': operator.add,
     '-': operator.sub,
     '*': operator.mul,
     '/': operator.truediv,
     '%': operator.mod,
     '**': operator.pow,
     '//':operator.floordiv
     }
    stack = []
    for token in expr.split(" "):
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1,op2))
        elif token:
            stack.append(float(token))
    return stack.pop()

if __name__ == '__main__':
    expr = input()
    print(calc(expr))
