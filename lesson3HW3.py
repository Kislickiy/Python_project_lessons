numbers = [56, 6, 7, 8, "test", 23, 189, "345", 8]
numbers_len = len(numbers)
numbers_len_half = numbers_len // 2
if numbers_len % 2 != 0:
    numbers_len_half += 1
numbers_part1 = numbers[:numbers_len_half]
numbers_part2 = numbers[numbers_len_half:]
numbers_2parts = [numbers_part1, numbers_part2]
print(numbers_2parts)