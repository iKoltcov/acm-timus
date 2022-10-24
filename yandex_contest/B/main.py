import sys

n = int(sys.stdin.readline())

max_lenght = 0
current_lenght = 0

for i in range(n):
    input = int(sys.stdin.readline())
    if input == 1:
        current_lenght += 1
        if current_lenght > max_lenght:
            max_lenght = current_lenght
    elif input == 0:
        current_lenght = 0

sys.stdout.write(f'{max_lenght}')
