import sys

n = int(sys.stdin.readline())
arr = [n * 2]

arr[0] = '(' * n + ')' * n
arr[-1] = '()' * n

for i in range(1, n):
    
    pass