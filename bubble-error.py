"""
Почему не работает код
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[i] > arr[+1]:
                arr[j], arr[i+1] = arr[i+1], arr[j]

if __name__ == "__main__":
    my_list = [5, 3, 9, 8, 6, 1, 7, 2, 4, 22, 0]
    bubble_sort(my_list)
    print("Отсортированный список:", my_list)
