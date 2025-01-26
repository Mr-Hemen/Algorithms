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

arr = [1, 2, 5, 3, 5, 1, -2]
values, max_repeat, most_repeated_items = find_most_repeated_items(arr)

print("Frequencies:", values)
print("Max repetition count:", max_repeat)
print("Most repeated items:", most_repeated_items)
