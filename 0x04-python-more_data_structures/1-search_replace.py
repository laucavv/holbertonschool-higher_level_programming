#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    idx = 0
    for i in new_list:
        if i == search:
            new_list[idx] = replace
        idx += 1
    return (new_list)
