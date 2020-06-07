def printnumbers(n):
    if n == 1:
        print(1, end=' ')
        return

    printnumbers(n-1)
    print(n, end=' ')


if __name__ == "__main__":
    n = int(input())
    printnumbers(n)
