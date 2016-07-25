
def is_palindrome(text):

    strip = {" ", ".", ","}
    length = len(text)
    forward = 0
    back = length-1

    while forward < length and back >= 0:
        if text[forward] in strip:
            forward+=1
        if text[back] in strip:
            back -=1
        if text[forward].lower() == text[back].lower():
            if back<=forward:
                return True
            back -=1
            forward +=1
        else :
            return  False




if __name__ == "__main__":
    print(is_palindrome("A nut for a jar of tuna."))
    print(is_palindrome("Anna"))
    print(is_palindrome("This is not a palindrome"))




