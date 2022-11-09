from math import sqrt
from sys import stdin, stdout

def isOne(position: int) -> bool:
    return ((sqrt(8 * position - 7) - 1) / 2) % 1 == 0

if __name__ == '__main__':
    n = int(stdin.readline())
    result = []
    for i in range(n):
        num = int(stdin.readline())
        result.append('1' if isOne(num) else '0')

    stdout.write(" ".join(result))
