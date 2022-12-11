import io
import sys
_INPUT = """\
3 34
1
8 13 26
"""

#sys.stdin = io.StringIO(_INPUT)



N, L = map(int, input().split())
K  = int(input())
A = list(map(int, input().split()))


def can_split(m, N, K, L, A):
    pre = 0
    cnt = 0
    for i in range(len(A)):
        if ((A[i] - pre) >= m) & ((L - A[i]) >= m):
            cnt += 1
            pre = A[i]
    if cnt >= K:
        return True
    else:
        return False

left, right = -1, L+1
while(right - left) > 1:
    mid = left + (right - left) // 2
    if can_split(mid, N, K, L, A):
        left = mid
    else:
        right = mid

print(left)