import sys
import collections

x = sys.stdin.readline()
y = sys.stdin.readline()

if collections.Counter(x) == collections.Counter(y):
    sys.stdout.write('1')
else:
    sys.stdout.write('0')
