from sys import stdin, stdout

if __name__ == '__main__':
    n = int(stdin.readline())
    max_score = 101

    teams = []
    for i in range(max_score + 1):
        teams.append([])

    for i in range(n):
        (id, score) = map(int, stdin.readline().split())
        teams[score].append(id)

    for i in range(max_score, -1, -1):
        if len(teams[i]) > 0:
            for j in range(len(teams[i])):
                stdout.write(f"{teams[i][j]} {i}\n")
