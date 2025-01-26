def limit_array(arr, min_val=None, max_val=None):
    min_check = lambda val: True if min_val is None else (val >= min_val)
    max_check = lambda val: True if max_val is None else (val <= max_val)

    return [val for val in arr if min_check(val) and max_check(val)]


# This function isn't optimal
def limit_array_2(arr, min_val=None, max_val=None):
    result = []

    if min_val and not max_val:
        for val in arr:
            if val >= min_val:
                result.append(val)
    elif max_val and not min_val:
        for val in arr:
            if val <= max_val:
                result.append(val)
    else:
        for val in arr:
            if max_val >= val >= min_val:
                result.append(val)

    return result