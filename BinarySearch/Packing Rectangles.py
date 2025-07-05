"""
    @author shyket
    @since 7/6/25
"""
# https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/A

w, h, n = list(map(int, input().split()))

l = 0
r = 1

def can_fit(x):
    return (x // w) * (x // h) >= n

while not can_fit(r):
    r *= 2

while l + 1 < r:
    m = (l + r) // 2

    if can_fit(m):
        r = m
    else:
        l = m

print(r)