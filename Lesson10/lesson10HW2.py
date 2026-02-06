import string

def first_word(text):
    punctuations = string.punctuation
    punctuations = punctuations.replace("'", "")
    while text[0] in string.punctuation:
        text = text[1:]
    for i in text:
        if i in punctuations:
            text = text.replace(i, " ")
    text = text.split()
    text = str(text[0])
    while text[-1] in string.punctuation:
        text = text[:-1]
    return text


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
