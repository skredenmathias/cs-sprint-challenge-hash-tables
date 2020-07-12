# Find the intersection between multiple lists of integers.

# we need to compute the numbers that exist in all lists.

# There can be up to 10 lists in the list of lists.

# The lists can contain up to roughly 1,000,000 elements each.

def intersection(arrays):
    result = {}
    array_length = 0
    result_arr = []

    for arr in arrays: # 100003 x 3
        for element in arr:
            if element not in result:
                result[element] = 1
            else:
                result[element] += 1
        array_length += 1

    for key, value in result.items():
        if value == array_length:
            result_arr.append(key)
    return result_arr


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))