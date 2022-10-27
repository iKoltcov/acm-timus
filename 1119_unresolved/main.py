from cmath import sqrt
from queue import Queue
from sys import stdin, stdout
from typing import Tuple

def distance(x1, y1, x2, y2) -> float:
    return sqrt( (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2) ).real

default_distance = distance(0, 0, 100, 100)
maxint = 2147483647

def packCoordinates(x: int, y: int, n: int) -> int:
    return y * n + x

def unpackCoordinates(i: int, n: int) -> Tuple[int, int]:
    return (int(i % n), int(i / n))

def deisktra(graph, start):
    score = [maxint] * len(graph)
    visited = [0] * len(graph)
    score[start] = 0
    queue = Queue()
    queue.put(start)

    while not queue.empty():
        v = queue.get()
        if visited[v] == 0:
            for i, w in graph[v]:
                if w != -1:
                    if score[i] > score[v] + w:
                        score[i] = score[v] + w
                    queue.put(i)
            visited[v] = 1

    return score

# with open('input.txt', 'r') as _input:
data = stdin.readline().split(' ')
n = int(data[0]) + 1
m = int(data[1]) + 1
k = int(stdin.readline())

diagonalable = []
for i in range(k):
    data = stdin.readline().split(' ')
    diagonalable.append( [int(data[0]), int(data[1])] )

nodes_len = n * m
graph = []

for i in range(nodes_len):
    adj = []
    x, y = unpackCoordinates(i, n)

    if x + 1 < n:
        adj.append( (packCoordinates(x + 1, y, n), 100) )

    if y + 1 < m:
        adj.append( (packCoordinates(x, y + 1, n), 100) )

    if x > 0:
        adj.append( (packCoordinates(x - 1, y, n), 100) )

    if y > 0:
        adj.append( (packCoordinates(x, y - 1, n), 100) )

    graph.append(adj)

for cell in diagonalable:
    x = cell[0] - 1
    y = cell[1] - 1

    ws = packCoordinates(x, y, n)
    ne = packCoordinates(x + 1, y + 1, n)

    graph[ ws ].append( (ne, default_distance) )
    graph[ ne ].append( (ws, default_distance) )

del diagonalable

result = round(deisktra(graph, 0)[packCoordinates(n - 1, m - 1, n)])

# with open('output.txt', 'w+') as _output:
stdout.write(f'{result}')
