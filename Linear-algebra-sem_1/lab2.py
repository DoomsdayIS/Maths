from math import *

P = open("input.txt", 'r')
M = open("output.txt", 'w')
st = P.readline()
vx, vy, vz = map(float, st.split())
st = P.readline()
ax, ay, az = map(float, st.split())
st = P.readline()
mx, my, mz = map(float, st.split())
st = P.readline()
wx, wy, wz = map(float, st.split())
if ax == 0:
    if ay > 0:
        if wx < vx:
            board_w = 1
        else:
            board_w = -1
    else:
        if wx < vx:
            board_w = -1
        else:
            board_w = 1
    if ay > 0:
        if mx < vx:
            board_m = 1
        else:
            board_m = -1
    else:
        if mx < vx:
            board_m = -1
        else:
            board_m = 1
else:
    # 1 Step ищем сторону мачты
    y_ot_m = (ay * mx - vx * (vy + ay) + vy * (vx + ax)) / ax
    if y_ot_m > my:
        board_m = 1
    else:
        board_m = -1
    if ax > 0:
        board_m = board_m * -1
    # 2 Step ищем сторону врага
    y_ot_w = (ay * wx - vx * (vy + ay) + vy * (vx + ax)) / ax
    if y_ot_w > wy:
        board_w = 1
    else:
        board_w = -1
    if ax > 0:
        board_w = board_w * -1
angle_m = acos(1 / sqrt(mx ** 2 + my ** 2 + 1))
angle_m = angle_m * board_m * 180 / pi
wx = wx - vx
wy = wy - vy
angle_w = acos((wx * ax + wy * ay) / (sqrt(wx ** 2 + wy ** 2) * sqrt(ax ** 2 + ay ** 2)))
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
