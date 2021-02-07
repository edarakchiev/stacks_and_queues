from collections import deque


def p_stat_init():
    n = int(input())
    petrol_stat = deque()
    for _ in range(n):
        petrol_stat.append(input())
    return petrol_stat, n


petrol_station, n = p_stat_init()


for big_circle in range(n):
    tank = 0
    is_valid = True
    for small_circle in range(n):
        current_station = petrol_station[small_circle]
        petrol, distance = current_station.split()
        petrol = int(petrol)
        distance = int(distance)
        tank += (petrol - distance)
        if tank < 0:
            is_valid = False
            petrol_station.append(petrol_station.popleft())
            break
    if is_valid:
        print(big_circle)
        break
