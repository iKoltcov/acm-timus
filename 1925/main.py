from sys import stdin, stdout

if __name__ == '__main__':
    (n, k) = map(lambda x: int(x), stdin.readline().split(' '))

    items = []
    g = 0
    d = 0
    for i in range(n):
        (input, actual) = map(lambda x: int(x), stdin.readline().split(' '))
        excepted = input - 2
        g += actual
        d += excepted

    result = (d - g) + (k - 2)

    if d + k <= g or result < 1:
        stdout.write("Big Bang!")
    else:
        stdout.write(f'{result}')