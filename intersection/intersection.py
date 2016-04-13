def bin_search(array, item):
    start = -1
    end = len(array)
    if item < array[0] or item > array[end - 1]:
        return None
    while start < end - 1:
        middle = (start + end) / 2
        if item >= array[middle]:
            start = middle
        else:
            end = middle
    if start >= 0 and array[start] == item:
        return start


def intersection(array1, array2):
    if len(array1) <= len(array2):
        min_array = array1
        max_array = array2
    else:
        min_array = array2
        max_array = array1
    pre_item = None
    found_index = None
    for item in min_array:
        if pre_item != item:
            found_index = bin_search(max_array, item)
            if found_index >= 0:
                yield max_array[found_index]
            pre_item = item
            continue
        if found_index > 0:
            if max_array[found_index - 1] == item:
                found_index -= 1
                yield item
                pre_item = item
            elif max_array[found_index - 1] != item:
                found_index = None
