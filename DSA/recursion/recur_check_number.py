from sys import setrecursionlimit


def check_number(arr, x):
    n = len(arr)

    if n == 1:
        return (x == arr[0])

    smallAns = check_number(arr[:n - 1], x)
    return smallAns or (x == arr[n - 1])


# Main
setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
if check_number(arr, x):
    print('true')
else:
    print('false')
