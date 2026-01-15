def quick_sort(arr, key_func, reverse=False):
    """Быстрая сортировка методом Хоара"""

    def partition(left, right):
        """Разделение массива относительно опорного элемента"""
        pivot_index = (left + right) // 2
        pivot_key = key_func(arr[pivot_index])

        i = left - 1
        j = right + 1

        while True:
            while True:
                i += 1
                if reverse:
                    if key_func(arr[i]) <= pivot_key:
                        break
                else:
                    if key_func(arr[i]) >= pivot_key:
                        break

            while True:
                j -= 1
                if reverse:
                    if key_func(arr[j]) >= pivot_key:
                        break
                else:
                    if key_func(arr[j]) <= pivot_key:
                        break

            if i >= j:
                return j

            arr[i], arr[j] = arr[j], arr[i]

    def _quick_sort(left, right):
        if left < right:
            p = partition(left, right)

            _quick_sort(left, p)
            _quick_sort(p + 1, right)

    if len(arr) <= 1:
        return arr

    _quick_sort(0, len(arr) - 1)
    return arr


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
