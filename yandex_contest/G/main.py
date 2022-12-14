from typing import List

def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return abs(x1 - x2) + abs(y1 - y2)

def bfs(start: int, end: int, graph: List[List[int]]):
    cost = [-1] * len(graph)
    cost[start] = 0
    queue = [start]

    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w == end:
                return cost[v] + 1

            if cost[w] == -1:
                queue.append(w)
                cost[w] = cost[v] + 1

    return cost[end]

result = -1

with open('input.txt', 'r') as _input:
    n = int(_input.readline())

    cities = []
    for i in range(n):
        data = _input.readline().split(' ')
        cities.append([ int(data[0]), int(data[1]) ])

    k = int(_input.readline())
    start_end = _input.readline().split(' ')

start = int(start_end[0]) - 1
end = int(start_end[1]) - 1

graph = []
for i in range(n):
    paths = []
    for j in range(n):
        if distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1]) <= k:
            paths.append(j)
    graph.append(paths)

result = bfs(start, end, graph)

with open('output.txt', 'w+') as _output:
    _output.write(f'{result}')