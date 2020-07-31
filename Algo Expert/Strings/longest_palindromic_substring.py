def longestPalindromicSubstring(string):
    output = ""
    n = len(string)
    if n == 1:
        return string
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if string[i: j + 1] == string[i: j + 1][::-1]:
                output = string[i: j + 1] if j - \
                    i + 1 >= len(output) else output
    return output


print(longestPalindromicSubstring("abaxyzzyxf"))
