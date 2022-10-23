from math import gcd
from sys import stdin, stdout

if __name__ == '__main__':
    input = stdin.readline().split(' ')
    n = int(input[0])
    m = int(input[1])

    M = max(0, max(n - 1, m - 1)) 
    N = max(0, min(n - 1, m - 1))

    stdout.write(f'{M + N - gcd(M, N)}\n')