num1 = int(input("Введіть число 1: "))
operator = input("Введіть знак дії: ")
num2 = int(input("Введіть число 2: "))
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/" and num2 != 0:
    result = num1 / num2
else: result = "Виконати дію неможливо"
print("Результат: " + str(result))