from sys import stdin, stdout

if __name__ == '__main__':
    data = stdin.readline().split(' ')

    n = int(data[0])
    m = int(data[1])
    y = int(data[2])

    output = []
    for i in range(1, m):
        if pow(i, n) % m == y:
            output.append(i)
    
    if len(output) == 0:
        stdout.write('-1')
    else:
        stdout.write(' '.join([str(x) for x in output]))