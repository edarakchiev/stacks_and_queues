from collections import deque

food_quantity = int(input())

data = list(map(int, input().split()))
order = deque()
max_order = 0

for el in data:
    if el > max_order:
        max_order = el
    order.append(el)

while order:
    if food_quantity >= order[0]:
        current_order = order.popleft()
        food_quantity -= current_order
    else:
        break

print(max_order)
if not order:
    print("Orders complete")
else:
    print(f"Orders left:", end='')
    for el in order:
        print(f" {el}", end="")
