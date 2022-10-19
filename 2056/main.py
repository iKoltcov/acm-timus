from typing import List

def main(n: int, array: List[int]) -> str:
    _3 = 0
    _5 = 0

    for x in array:
        if x == 3:
            _3 += 1
        elif x == 5:
            _5 += 1


    if _3 > 0:
        return 'None'
    
    if _5 == n:
        return 'Named'

    average = sum(array) / n
    if average >= 4.5:
        return 'High'
    else:
        return 'Common'

if __name__ == "__main__":
    n = int(input())
    array = list()
    for i in range(n):
        array.append(int(input()))

    print(main(n, array))