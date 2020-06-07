
def sum_array(arr):
    n = len(arr)

    if n == 1:
        return arr[0]

    return sum_array(arr[:n - 1]) + arr[n - 1]


if __name__ == "__main__":
    from sys import setrecursionlimit
    setrecursionlimit(11000)
    n = int(input())
    arr = list(int(i) for i in input().strip().split(' '))
    print(sum_array(arr))
