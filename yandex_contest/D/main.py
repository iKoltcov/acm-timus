import sys

def generate(current: str, open: int, closed: int, n: int):
    if len(current) == n*2:
        sys.stdout.write(f'{current}\n')
        return

    if open < n:
        generate(current + '(', open + 1, closed, n)

    if closed < open:
        generate(current + ')', open, closed + 1, n)

n = int(sys.stdin.readline())

generate('', 0, 0, n)