def palindrome(word):
    return True if list(word) == list(reversed((word))) else False

print(palindrome('기러기러기'))