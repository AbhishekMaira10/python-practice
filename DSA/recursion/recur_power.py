from sys import setrecursionlimit


def power(x, n):
    if n == 0:
        return 1
    return x*power(x, n-1)


# Main
setrecursionlimit(11000)
x, n = list(int(i) for i in input().strip().split(' '))
print(power(x, n))
