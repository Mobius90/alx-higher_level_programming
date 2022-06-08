#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return None
    result = 0
    nlist = []
    for i in my_list:
        if i not in nlist:
            result = result + i
        nlist.append(i)
    return result
