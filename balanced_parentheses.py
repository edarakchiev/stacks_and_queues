data = input()
stack = []

for i in range(len(data)):
    if data[i] in "({[":
        stack.append(data[i])

    if stack:
        if stack[-1] == "(" and data[i] == ")":
            stack.pop()
        elif stack[-1] == "[" and data[i] == "]":
            stack.pop()
        elif stack[-1] == "{" and data[i] == "}":
            stack.pop()
    else:
        stack.append(data[i])
if stack:
    print("NO")
else:
    print("YES")