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
ошибка в самом алгоритме, надо писать return quick_sort(less) + [pivot] + quick_sort(greater)
вместо return quick_sort(less) + pivot + quick_sort(greater)
"""

"""
также можно спросить, почему не работает return quick_sort(less) + list(pivot) + quick_sort(greater)
ответ: потому что pivot будет единственным элоементом, а не итеррируемым объектом,
а list делает список из элементов итерируемого объекта, например строки
"""