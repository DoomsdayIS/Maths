from math import *

P = open("input.txt", 'r')
M = open("output.txt", 'w')
st = P.readline()
v = list(map(float, st.split()))
st = P.readline()
a = list(map(float, st.split()))
st = P.readline()
m = list(map(float, st.split()))
st = P.readline()
w = list(map(float, st.split()))
if a[0] == 0:
    if a[1] > 0:
        if w[0] < v[0]:
            board_w = 1
        else:
            board_w = -1
    else:
        if w[0] < v[0]:
            board_w = -1
        else:
            board_w = 1
    if a[1] > 0:
        if m[0] < v[0]:
            board_m = 1
        else:
            board_m = -1
    else:
        if m[0] < v[0]:
            board_m = -1
        else:
            board_m = 1
else:
    # 1 Step ищем сторону мачты
    y_ot_m = (a[1] * m[0] - v[0] * (a[1] + v[1]) + v[1] * (a[0] + v[0])) / a[0]
    if y_ot_m > m[1]:
        board_m = 1
    else:
        board_m = -1
    if a[0] > 0:
        board_m = board_m * -1
    # 2 Step ищем сторону врага
    y_ot_w = (a[1] * w[0] - v[0] * (a[1] + v[1]) + v[1] * (a[0] + v[0])) / a[0]
    if y_ot_w > w[1]:
        board_w = 1
    else:
        board_w = -1
    if a[0] > 0:
        board_w = board_w * -1
angle_m = acos(1 / sqrt(m[0] ** 2 + m[1] ** 2 + 1))
angle_m = angle_m * board_m * 180 / pi
w[0] = w[0] - v[0]
w[1] = w[1] - v[1]
angle_w = acos((w[0] * a[0] + w[1] * a[1]) / (sqrt(w[0] ** 2 + w[1] ** 2) * sqrt(a[0] ** 2 + a[1] ** 2)))
angle_w = 90 - angle_w * 180 / pi
if abs(angle_m) <= 60 and abs(angle_w) <= 60:
    M.write(str(board_w))
    M.write("\n")
    M.write(str(round(angle_w, 2)))
    M.write("\n")
    M.write(str(round(angle_m, 2)))
    M.write("\n")
    M.write("PLS")
else:
    M.write("0")
P.close()
M.close()
