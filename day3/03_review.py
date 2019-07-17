user_word = input("단어를 입력하세요 : ")

def palindrome(user_word):
    len_word = len(user_word)
    list_word = list(user_word)
    for i in range(int(len_word/2)):
        if list_word[i] != list_word[-1-i]:
            return 'False'
        else:
            return 'True'
print(palindrome(user_word))