numbers = [12, 3, 4, 10]
# => [10, 12, 3, 4]
if len(numbers) > 1:
    result = numbers.pop(-1)
    numbers.insert(0, result)
print(numbers)

numbers = [1]
# => [1]
if len(numbers) > 1:
    result = numbers.pop(-1)
    numbers.insert(0, result)
print(numbers)

numbers = []
# => []
if len(numbers) > 1:
    result = numbers.pop(-1)
    numbers.insert(0, result)
print(numbers)

numbers = [12, 3, 4, 10, 8]
# => [8, 12, 3, 4, 10]
if len(numbers) > 1:
    result = numbers.pop(-1)
    numbers.insert(0, result)
print(numbers)