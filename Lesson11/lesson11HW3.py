def is_even(number):
    if str(number)[-1] == "2" or str(number)[-1] == "4" or str(number)[-1] == "6" or str(number)[-1] == "8" or str(number)[-1] == "0":
        return True
    else:
        return False

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
assert is_even(10) == True, 'Test4'
assert is_even(0) == True, 'Test5'