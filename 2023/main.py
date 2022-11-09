from sys import stdin, stdout

lists = [
    [ "Alice", "Ariel", "Aurora", "Phil", "Peter", "Olaf", "Phoebus", "Ralph", "Robin" ],
    [ "Bambi", "Belle", "Bolt", "Mulan", "Mowgli", "Mickey", "Silver", "Simba", "Stitch" ],
    [ "Dumbo", "Genie", "Jiminy", "Kuzko", "Kida", "Kenai", "Tarzan", "Tiana", "Winnie" ],
]

if __name__ == '__main__':
    n = int(stdin.readline())

    current = 0
    steps = 0
    for i in range(n):
        name = str(stdin.readline().replace('\n', ''))

        for j in range(len(lists)):
            if name in lists[j]:
                steps += abs(current - j)
                current = j
                break

    stdout.write('%s' % (steps, ))
