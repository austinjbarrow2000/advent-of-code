def merge(arr_one, arr_two):
    result = []

    while len(arr_one) > 0 and len(arr_two) > 0:
        if arr_one[0] > arr_two[0]:
            result.append(arr_one.pop(0))
        else:
            result.append(arr_two.pop(0))
    while len(arr_one) > 0:
        result.append(arr_one.pop(0))
    while len(arr_two) > 0:
        result.append(arr_two.pop(0))

    return result


def mergesort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    arr_one = mergesort(arr[:mid])
    arr_two = mergesort(arr[mid:])
    result = merge(arr_one, arr_two)
    return result
