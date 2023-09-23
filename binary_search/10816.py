N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))
cards.sort()

def binary_search(target, left, right):
    if left > right:
        return 0

    mid = (left + right) // 2
    if cards[mid] == target:
        return count.get(target)
    elif cards[mid] < target:
        return binary_search(target, mid + 1, right)
    else:
        return binary_search(target, left, mid - 1)

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for num in numbers:
    print(binary_search(num, 0, len(cards)-1), end=" ")