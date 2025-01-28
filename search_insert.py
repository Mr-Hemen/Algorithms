def search_insert(array, value):
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        mid = (start_index + end_index) // 2
        if value < array[mid]:
            end_index = mid - 1
        else:
            start_index = mid + 1

    # insert value to array
    array[start_index:start_index] = [value]

    return array
