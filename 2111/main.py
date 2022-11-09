from sys import stdin, stdout

if __name__ == '__main__':
    n = int(stdin.readline())
    d = sorted(map(lambda x: int(x), stdin.readline().split(' ')))
    size = sum(d)
    result = 0

    for i in d:
        result += (size * i) + ((size - i) * i)
        size -= i

    stdout.write(f'{result}\n')