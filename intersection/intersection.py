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
    max_array = max(array1, array2)
    min_array = min(array1, array2)
    result = []
    pre_item = None
    found_index = None
    for item in min_array:
        if pre_item == item and found_index > 0 and max_array[found_index-1] == item:
            found_index -= 1
            result.append(item)
            pre_item = item
        elif pre_item == item and found_index > 0 and max_array[found_index-1] != item:
            found_index = None
        elif pre_item != item:
            found_index = bin_search(max_array, item)
            if found_index or found_index == 0:
                result.append(max_array[found_index])
            pre_item =item
    return result






