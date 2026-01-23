import string
def is_palindrome(text):
    text = text.replace(" ", "")
    text = text.lower()
    final_text = ""
    for char in text:
        if char not in string.punctuation:
            final_text += char
    reverse_text = final_text[::-1]
    if reverse_text == final_text:
        palindrome = True
    else:
        palindrome = False
    return palindrome
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")