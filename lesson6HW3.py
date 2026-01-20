input_data = int(input("Enter a number: "))

while input_data > 9:
    input_data_str = str(input_data)
    input_data = 1
    for i in input_data_str:
        input_data *= int(i)
print(input_data)
