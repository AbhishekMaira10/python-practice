def caesarCipherEncryptor(string, key):
    output = ""
    for char in string:
        x = ord(char) + key % 26
        output += chr(x) if x <= 122 else chr(x - 26)
    return output


print(caesarCipherEncryptor("oyz", 52))
