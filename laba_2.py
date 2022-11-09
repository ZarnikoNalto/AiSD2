import math
import matplotlib.pyplot as plt
points = [(150, 4), (31, 8), (84, 1000), (100, 180), (37, 21), (15, 17)]
plt.scatter([150, 31, 37, 84, 100, 15], [4, 8, 21, 1000, 180, 17])
plt.show()

def merge_sort(arr, coord):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    pointsleft = arr[:mid]
    pointsright = arr[mid:]

    left_sorted = merge_sort(pointsleft, coord)
    right_sorted = merge_sort(pointsright, coord)
    cmbo = merge(left_sorted, right_sorted, coord)
    return cmbo


def merge(first_dist, sec_dist, coord):
    i = j = 0
    empty_arr = []

    if coord == 'x':
        coord = 0
    elif coord == 'y':
        coord = 1

    while i < len(first_dist) and j < len(sec_dist):
        if first_dist[i][coord] <= sec_dist[j][coord]:
            empty_arr.append(first_dist[i])
            i += 1

        elif sec_dist[j][coord] < first_dist[i][coord]:
            empty_arr.append(sec_dist[j])
            j += 1

    while i < len(first_dist) and j == len(sec_dist):
        empty_arr.append(first_dist[i])
        i += 1

    while j < len(sec_dist) and i == len(first_dist):
        empty_arr.append(sec_dist[j])
        j += 1

    return empty_arr


def first_sort(points):
    Px = merge_sort(points, 'x')
    Py = merge_sort(points, 'y')
    return Px, Py


Px, Py = first_sort(points)


def find_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def brute_force(arr):
    size = len(arr)
    minimum_distance = find_dist(arr[0], arr[1])
    target_pair = (arr[0], arr[1])

    if len(arr) == 2:
        return find_dist(arr[0], arr[1]), arr[0], arr[1]

    for i in range(0, size):
        for j in range(i + 1, size):
            distance = find_dist(arr[i], arr[j])
            if distance < minimum_distance:
                minimum_distance = distance
                target_pair = (arr[i], arr[j])

    return minimum_distance, target_pair


def closest_pair(Px, Py):
    if len(Px) <= 3:
        return brute_force(Px)

    midpoint_x = len(Px) // 2
    Qx = Px[:midpoint_x]
    Rx = Px[midpoint_x:]
    median_x = Px[midpoint_x]
    Qy, Ry = [], []

    for point in Py:
        if point[0] < int(median_x[0]):
            Qy.append(point)
        else:
            Ry.append(point)

    min_distance_left = closest_pair(Qx, Qy)
    min_distance_right = closest_pair(Rx, Ry)
    min_distance = min(min_distance_left, min_distance_right)
    x_bar = Qx[-1][0]
    Sy = []

    for y in Py:
        if x_bar - min_distance[0] < y[0] < x_bar + min_distance[0]:
            Sy.append(y)

    for i in range(len(Sy) - 1):
        for j in range(i + 1, min(i + 7, len(Sy))):
            points = Sy[i]
            points_close = Sy[j]
            dist = find_dist(points, points_close)

            if dist < min_distance[0]:
                min_distance = (dist, points, points_close)
                distance = min_distance
    return min_distance

distance = closest_pair(Px, Py)
print(distance)
