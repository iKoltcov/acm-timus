from sys import stdin, stdout

if __name__ == '__main__':
    n = int(stdin.readline())

    data = []
    for i in range(n):
        data.append(stdin.readline().replace('\n', '').split(' '))

    result = []
    for k in range(n * 2):
        for j in range(k + 1):
            i = k - j
            if i < n and j < n:
                result.append(data[i][j])

    stdout.write(" ".join(result))