def difference(*args):
    args_list = []
    for arg in args:
        args_list.append(arg)
    if len(args_list) > 0:
        max_value = max(args_list)
        min_value = min(args_list)
        result = max_value - min_value
        result = round(result, 2)
    else:
        result = 0
    return result

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
