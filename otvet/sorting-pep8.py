"""
Нужно отсортировать массив из чисел
"""
nums = eval(input())
k1 = -1
k2 = 0
n = len(nums)
nums = [
    nums[i] if nums[i] != 0 else (
        (nums[k1], nums[k2], k1, k2 := k2 + 1) if (k1 != -1 and k1 < n)
        else (nums[k2], nums[i], k2 + 1)
    ) if nums[i] == 1 else (nums[i], k1 := k2)[0]
    for i in range(n)
    ]
print(nums)
