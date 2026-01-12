
# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88
# [1, 3, 5] => 30
# [6] => 36
# [] => 0

numbers = [0, 1, 7, 2, 4, 8]
# numbers = [1, 3, 5]
# numbers = [6]
# numbers = []
numbers_pairs = numbers[::2]
numbers_pairs_sum = 0
for i in numbers_pairs:
    numbers_pairs_sum += i
if len(numbers) > 0:
    result = numbers_pairs_sum * numbers[-1]
else:
    result = 0
print(result)

