n = int(input())
stack = []

for _ in range(n):
    data = input().split()
    num = int(data[0])
    if num == 1:
        stack.append(int(data[1]))
    elif num == 2 and len(stack) > 0:
        stack.pop()
    elif num == 3 and len(stack) > 0:
        max_num = max(stack)
        print(max_num)
    elif num == 4 and len(stack) > 0:
        min_num = min(stack)
        print(min_num)
stack_final = []
while stack:
    stack_final.append(str(stack.pop()))

print(", ".join(stack_final))