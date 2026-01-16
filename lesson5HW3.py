# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

import string

input_data = input("Enter a hashtag: ")
max_length = 140
input_data = input_data.title()
input_data = input_data.replace(" ", "")
for char in string.punctuation:
    input_data = input_data.replace(char, "")
if len(input_data) > max_length:
    input_data = input_data[:max_length]
input_data = "#" + input_data
print(input_data)
