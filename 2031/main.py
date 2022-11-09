from sys import stdin, stdout

if __name__ == '__main__':
    n = int(stdin.readline())

    if (n > 4):
        stdout.write("Glupenky Pierre")
    else:
        arr = [ "16", "06", "68", "88" ]
        stdout.write(" ".join(arr[0:n]))
