def longestCommonPrefix(A):
    """[python solution using zip method]

    Args:
        A ([List of Strings]): [input]

    Returns:
        [String]: [Longest common prefix of all the strings]
    """
    str = ""
    for x in zip(*A):
        if len(set(x)) == 1:
            str += x[0]
        else:
            break
    return str


print(longestCommonPrefix(["abab", "ab", "abcd"]))
