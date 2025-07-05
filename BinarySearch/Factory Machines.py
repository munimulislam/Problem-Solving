"""
    @author shyket
    @since 7/6/25
"""
# https://cses.fi/problemset/task/1620/

n, t = list(map(int, input().split()))
arr = list(map(int, input().split()))

l = 0
r = 1

def can_produce(time):
    total = 0
    for i in arr:
        total += (time // i)

    return total >= t


while not can_produce(r):
    r *= 2

while l + 1 < r:
    m = (l + r) // 2

    if can_produce(m):
        r = m
    else:
        l = m

print(r)