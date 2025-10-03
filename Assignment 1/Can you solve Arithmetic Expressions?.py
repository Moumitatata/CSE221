#Can you solve Arithmetic Expressions?
x = int(input())
for i in range(x):
    a = input().split(' ')
    b = int(a[1])
    c = int(a[3])
    if a[2] == '+':
        res = float(b + c)
        print(res)
    if a[2] == '-':
        print(float(b - c))
    if a[2] == '*':
        print(float(b * c))
    if a[2] == '/':
        print(float(b / c))
