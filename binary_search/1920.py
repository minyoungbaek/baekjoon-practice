N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

def binary_search(x, start, end):
    if start > end:
        return 0
    mid = (start+end) // 2
    if x == A[mid]:
        return 1
    elif A[mid] > x:
        return binary_search(x, start, mid-1)
    else:
        return binary_search(x, mid+1, end)

for number in T:
    start = 0
    end = len(A) - 1
    print(binary_search(number, start, end))