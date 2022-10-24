with open('input.txt', 'r') as _input:
    with open('output.txt', 'w+') as _output:
        n = int(_input.readline())

        if n != 0:
            current_value = int(_input.readline())
            _output.write(f'{current_value}\n')

            for i in range(n - 1):
                new_value = int(_input.readline())

                if current_value != new_value:
                    _output.write(f'{new_value}\n')
                    current_value = new_value
