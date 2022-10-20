from sys import stdin, stdout

class Node:
    def __init__(self, id: int = None, value: int = None):
        self.left = None
        self.ids = []
        if id != None:
            self.ids.append(id)
        self.value = value
        self.right = None

    def add_node(self, id: int, value: int):
        if self.value == None:
            self.ids.append(id)
            self.value = value
            return

        if self.value == value:
            self.ids.append(id)
            return

        if self.value > value:
            if self.left == None:
                self.left = Node(id, value)
                return
            else:
                self.left.add_node(id, value)
                return

        if self.value < value:
            if self.right == None:
                self.right = Node(id, value)
                return
            else:
                self.right.add_node(id, value)
                return

    def print_desc(self):
        if self.right != None:
            self.right.print_desc()

        for id in self.ids:
            stdout.write('%s %s\n' % (id, self.value))

        if self.left != None:
            self.left.print_desc()


if __name__ == '__main__':
    n = int(stdin.readline())
    root = Node()
    teams_set = set()

    for i in range(n):
        data = stdin.readline().split(' ')
        id = int(data[0])
        value = int(data[1])

        if id not in teams_set:
            teams_set.add(id)
            root.add_node(id, value)

    root.print_desc()
