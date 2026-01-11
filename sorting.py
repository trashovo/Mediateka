def quick_sort(arr, key_func, reverse=False):
    """Быстрая сортировка (метод Хоара)."""
    if len(arr) <= 1:
        return arr

    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    pivot_key = key_func(pivot)

    left = []
    middle = []
    right = []

    for item in arr:
        item_key = key_func(item)

        if item_key == pivot_key:
            middle.append(item)
        elif (reverse and item_key > pivot_key) or (not reverse and item_key < pivot_key):
            left.append(item)
        else:
            right.append(item)

    return quick_sort(left, key_func, reverse) + middle + quick_sort(right, key_func, reverse)


def multi_key_sort(arr, keys):
    """Сортировка по нескольким ключам с использованием быстрой сортировки"""
    if not arr or not keys:
        return arr

        def compare_func(item):
        result = []
        for key_func, reverse in keys:
            value = key_func(item)
            if isinstance(value, (int, float)):
                if reverse:
                    result.append(-value)
                else:
                    result.append(value)

            elif isinstance(value, str):
                if reverse:
                    inverted = ''.join(chr(0x10FFFF - ord(c)) for c in value)
                    result.append(inverted)
                else:
                    result.append(value)
        return result


    return quick_sort(arr, compare_func)

