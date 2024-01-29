def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    my_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = quick_sort(my_list)
    print("Отсортированный список:", sorted_list)


"""
тут ошибка была чисто в том, что не было центрального элемента, т.е. просто ошибка в алгоритме
return quick_sort(less) + quick_sort(greater)
а нужно:
return quick_sort(less) + [pivot] + quick_sort(greater)
"""