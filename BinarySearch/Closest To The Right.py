"""
    @author shyket
    @since 7/5/25
"""

"""
    @author shyket
    @since 7/5/25
"""

# https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/C

m, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

n = len(arr)

for x in query:
    low = -1
    high = n

    while low + 1 < high:
        mid = low + (high - low) // 2

        if arr[mid] >= x:
            high = mid
        else:
            low = mid

    print(high+1)
