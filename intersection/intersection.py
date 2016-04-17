def left_bin_search(array, item):
    start = -1
    end = len(array)
    if item < array[0] or item > array[end - 1]:
        return None
    while start < end - 1:
        middle = (start + end) / 2
        if item > array[middle]:
            start = middle
        else:
            end = middle
    if end < len(array) and array[end] == item:
        return end


def right_bin_search(array, item, start):
    if not start:
        start = -1
    end = len(array)
    if item < array[0] or item > array[-1]:
        return None
    while start < end - 1:
        mid = (start + end) / 2
        if item >= array[mid]:
            start = mid
        else:
            end = mid
    if start >= 0 and array[start] == item:
        return start


def intersection(array1, array2):
    if len(array1) > len(array2):
        tmp = array1
        array1 = array2
        array2 = tmp
    pre_item, last_found_index, found_index = None, None, None
    for item in array1:
        if pre_item != item:
            found_index = right_bin_search(array2, item, last_found_index)
            last_found_index = found_index
            if found_index >= 0:
                yield item
        elif found_index > 0:
            if array2[found_index - 1] == item:
                found_index -= 1
                yield item
            else:
                found_index = None
        pre_item = item

