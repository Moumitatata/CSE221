#Odd or Even?
import sys
x = int(sys.stdin.readline())

for i in range(x):
    a = int(input())
    if a%2 == 0:
        print(f'{a} is an Even number.')
    else:
        print(f'{a} is an Odd number.')