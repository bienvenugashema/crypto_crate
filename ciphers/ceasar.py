def caesar_cipher(text, shift, mode="encrypt"):
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    result = ''
    
    for char in text:
        if char in upper_letters:
            if mode == "encrypt":
                index = (upper_letters.index(char) + shift) % 26
                result += upper_letters[index]
            else:
                index = (upper_letters.index(char) - shift) % 26
                result += upper_letters[index]
        elif char in lower_letters:
            if mode == "encrypt":
                index = (lower_letters.index(char) + shift) % 26
                result += lower_letters[index]
            else:
                index = (lower_letters.index(char) - shift) % 26
                result += lower_letters[index]
        else:
            result += char    
    return result
