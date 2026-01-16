import string
import keyword

forbidden_symbols = string.punctuation.replace("_", "")
upper_letters = string.ascii_uppercase
var_name_input = input("Enter var name: ")

if len(var_name_input) == 0:
    print(False)

elif var_name_input in keyword.kwlist:
    print(False)

elif var_name_input[0].isnumeric():
    print(False)

elif "__" in var_name_input:
    print(False)


elif any(char.isupper() for char in var_name_input):
    print(False)

elif " " in var_name_input:
    print(False)

else:
    forbidden = string.punctuation.replace("_", "")
    if any(char in forbidden for char in var_name_input):
        print(False)
    else:
        print(True)