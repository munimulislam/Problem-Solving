"""
    @author shyket
    @since 7/5/25
"""
# https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/D

m = int(input())
arr = list(map(int, input().split()))
k = int(input())

n = len(arr)
arr.sort()

for x in range(k):
    l, r = list(map(int, input().split()))

    left = -1
    right = n

    min_l_pos = 0
    min_r_pos = 0

    while left + 1 < right:
        mid = left + (right - left) // 2

        if arr[mid] >= l:
            right = mid
        else:
            left = mid

    min_l_pos = right

    left = -1
    right = n

    while left + 1 < right:
        mid = left + (right - left) // 2

        if arr[mid] <= r:
            left = mid
        else:
            right = mid

    min_r_pos = left

    print(min_r_pos - min_l_pos + 1)

