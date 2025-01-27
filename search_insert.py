def search_insert(array, value):
    start_index = 0
    end_index = len(array) - 1
    mid = end_index // 2
    new_array = []
    
    while start_index <= end_index:
        if value < array[mid]:
            mid -= 1
            end_index = mid
        else:
            mid += 1
            start_index = mid

    if start_index == 0:
            new_array.append(value)
            new_array.extend(array)
    elif 0 < start_index < len(array):
        new_array.extend(array[:start_index])
        new_array.append(value)
        new_array.extend(array[start_index:])
    else:
        new_array.extend(array)
        new_array.append(value)

    return new_array
