from queue import Queue
from sys import stdin, stdout
from typing import List

class Person:
    def __init__(self, name: str, teams: List[str]) -> None:
        self.name = name
        self.teams = teams

def bfs(graph, start):
    cost = [-1] * len(graph)
    queue = Queue()
    queue.put(start)
    cost[start] = 0

    while not queue.empty():
        v = queue.get()
        for w in graph[v]:
            if cost[w] == -1:
                cost[w] = cost[v] + 1
                queue.put(w)

    return cost

# with open('input.txt', 'r') as _input:
n = int(stdin.readline())
teams = []
persons = {}

for i in range(n):
    data = stdin.readline().replace('\n', '').split(' ')
    teams.append(data)
    for person in data:
        if person not in persons:
            persons[person] = []
        persons[person].append(i)

persons = dict(sorted(persons.items()))

persons_ids = {}
i = 0
for name in persons.keys():
    persons_ids[name] = i
    i += 1

graph = []
i = 0
for name, playedIn in persons.items():
    adj = set()
    for team_id in playedIn:
        for teammates in teams[team_id]:
            if name != teammates:
                adj.add(persons_ids[teammates])
    graph.append(list(adj))
    i += 1

if 'Isenbaev' in persons_ids:
    result = bfs(graph, persons_ids['Isenbaev'])
else:
    result = [-1] * len(persons_ids)

# with open('output.txt', 'w+') as _output:
names = list(persons.keys())
for i in range(len(result)):
    output = result[i] if result[i] != -1 else 'undefined'
    stdout.write(f'{names[i]} {output}\n')