def countdigits(n):
    x = int(n/10)

    if x == 0:
        return 1

    return 1 + countdigits(x)


if __name__ == "__main__":
    n = int(input())
    print(countdigits(n))
