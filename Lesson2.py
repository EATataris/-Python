#1
# default_list = [1, 'Hello', None, True, [2, 3], {'x': 1, 'y': 2}]
# for i in default_list:
#     print(f'{i} - {type(i)}')

#2
def split_list(list):
    lists = []
    final_list = []
    while len(list) > 2:
        lists.append(list[:2])
        list = list[2:]
    else:
        lists.append(list[:len(list)])
    for i in lists:
        i.reverse()
        for j in i:
            final_list.append(j)
    return final_list


ls = [1, 2, 3, 4, 5]
print(split_list(ls))