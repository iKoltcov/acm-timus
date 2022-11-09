from queue import Queue
from sys import stdin, stdout
from typing import Tuple

diag_distance = 141.4213562373095
maxint = 2147483647

def packCoordinates(x: int, y: int, n: int) -> int:
    return y * n + x

def unpackCoordinates(i: int, n: int) -> Tuple[int, int]:
    return (i % n, i // n)

def deisktra(graph, start, end):
    score = [maxint] * len(graph)
    visited = [False] * len(graph)
    score[start] = 0
    queue = Queue()
    queue.put(start)

    while not queue.empty():
        v = queue.get()
        if visited[v] == False:
            for i, w in graph[v]:
                if w != -1:
                    if score[i] > score[v] + w:
                        score[i] = score[v] + w
                    queue.put(i)
            visited[v] = True

    return score[end]

if __name__ == '__main__':
    (n, m) = map(int, stdin.readline().split(' '))

    n += 1
    m += 1

    nodes_len = n * m
    graph = []

    for i in range(nodes_len):
        adj = []
        x, y = unpackCoordinates(i, n)
        if x + 1 < n:
            adj.append( (packCoordinates(x + 1, y, n), 100) )
        if y + 1 < m:
            adj.append( (packCoordinates(x, y + 1, n), 100) )
        graph.append(adj)

    k = int(stdin.readline())
    for i in range(k):
        (x, y) = map(int, stdin.readline().split(' '))
        ws = packCoordinates(x - 1, y - 1, n)
        ne = packCoordinates(x, y, n)
        graph[ ws ].append( (ne, diag_distance) )

    result = round(deisktra(graph, 0, packCoordinates(n - 1, m - 1, n)))
    stdout.write(f'{result}')
