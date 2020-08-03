def isPalindrome(A):
    output = ""
    for i in A:
        if i.isalnum():
            output = output + i.lower()
    return 1 if output == output[::-1] else 0


print(isPalindrome("A man, a plan, a canal: Panama"))
