import string

input_data = input("Enter two letters with '-': ")
all_letters = string.ascii_letters

if len(input_data) == 3:
    first_letter = input_data[0]
    second_letter = input_data[2]
    sep = input_data[1]

    if first_letter.isalpha() and second_letter.isalpha() and sep == "-":
        start_index = all_letters.find(first_letter)
        end_index = all_letters.find(second_letter)

        if start_index > end_index:
            start_index, end_index = end_index, start_index

        result = all_letters[start_index:end_index+1]
        print(result)

    else:
        print("Invalid input")

else:
    print("Invalid input")

