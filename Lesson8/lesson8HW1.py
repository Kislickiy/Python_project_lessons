
def add_one(some_list):
    some_list_str = ""
    for i in some_list:
        some_list_str += str(i)
    some_list_num = int(some_list_str)
    some_list_num_1 = some_list_num + 1
    result_list = []
    for i in str(some_list_num_1):
        i = int(i)
        result_list.append(i)
    return result_list
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
