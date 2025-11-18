#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes an element at a specific position in a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    # idx-dən sonrakı elementləri bir sola sürüşdürüb sonuncunu silirik
    for i in range(idx, len(my_list) - 1):
        my_list[i] = my_list[i + 1]
    my_list[:] = my_list[:-1]
    return my_list
