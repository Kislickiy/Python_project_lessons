def common_elements():
    list3 = []
    list5 = []
    for i in list(range(100)):
        if i % 3 == 0:
            list3.append(i)
        if i % 5 == 0:
            list5.append(i)
    dict_3_5 = set(list3) & set(list5)
    return dict_3_5

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
