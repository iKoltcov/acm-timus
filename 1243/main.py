from sys import stdin, stdout

if __name__ == '__main__':
    data = int(stdin.readline())
    stdout.write(str(data % 7))