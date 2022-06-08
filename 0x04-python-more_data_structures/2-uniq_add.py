#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return None
    result = 0
    nlist = []
    for i in my_list:
        count = 0
        for j in nlist:
            if i == j:
                count = count + 1
                continue
        if count > 0:
            continue
        nlist.append(i)
    for i in nlist:
        result = result + i
    return result
