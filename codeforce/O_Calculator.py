expression = input()
if '/' in expression:
    expression = expression.replace('/', '//')
try:
    result = eval(expression)
    print(result)
except ZeroDivisionError:
    print()
except Exception as e:
    print()
