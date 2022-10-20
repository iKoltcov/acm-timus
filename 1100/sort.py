from sys import stdin, stdout

def countingSort(array):
    size = len(array)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

if __name__ == '__main__':
    n = int(stdin.readline())
    teams_set = set()
    teams = []

    for i in range(n):
        data = stdin.readline().split(' ')
        id = int(data[0])
        value = int(data[1])

        if id not in teams_set:
            teams_set.add(id)
            teams.append([id, value])

    countingSort(teams)

    for team in teams:
        stdout.write('%s %s\n' % (team[0], team[1]))
