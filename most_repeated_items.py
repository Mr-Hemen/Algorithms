def find_most_repeated_items(arr):
    values = {}
    most_repeated_items = []


    for val in arr:
        if val in values:
            values[val] += 1
        else:
            values[val] = 1

    max_repeat = max(values.values())

    for key in values.keys():
        if max_repeat == values[key]:
            most_repeated_items.append(key)


    return values, max_repeat, most_repeated_items

a = [1, 2, 5, 3, 5, 1, -2]
print(find_most_repeated_items(a))
