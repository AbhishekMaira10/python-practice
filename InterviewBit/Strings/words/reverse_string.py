def solve(A):
    l = A.strip().split(' ')
    str = ''
    for i in reversed(l):
        if(i != ' '):
            str = str + i + " "
    return str


print(solve("j"))
