from math import ceil
import sys

def qsort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)

        return qsort(less) + equal + qsort(greater)
    else:
        return array

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

if len(arr) % 2 == 0:
    sys.stdout.write(f'{ (arr[ceil(n / 2)] + arr[ceil(n / 2) + 1]) / 2 }')
else:
    sys.stdout.write(f'{ arr[ceil(n / 2)] }')
