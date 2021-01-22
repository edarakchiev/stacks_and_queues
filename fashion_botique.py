box = list(map(int, input().split()))
capacity = int(input())

rack_counter = 1
current_sum = 0

while box:
    current_piece = box.pop()
    if current_sum + current_piece <= capacity:
        current_sum += current_piece
    else:
        rack_counter += 1
        current_sum = current_piece
print(rack_counter)
