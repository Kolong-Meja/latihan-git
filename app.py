# latihan git dan program python pertamaku

def forbiddenWords():
    forbidden_words = ["fuck", "shit", "asshole", "dick", "pussy"]
    return forbidden_words

def showMessage():
    isForbiddenWord = False

    while isForbiddenWord != True:
        user_input = input("input your word: ").lower()
        if user_input in forbiddenWords():
            isForbiddenWord = True
            while isForbiddenWord:
                errorMsg = ValueError("please input correctly!")
                new_user_input = input("input again your word: ")
                if new_user_input in forbiddenWords():
                    print(errorMsg)
                    continue
                else: return new_user_input
        else: return user_input
print(showMessage())
