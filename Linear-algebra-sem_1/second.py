from math import *
v = list(map(float,input().split()))
a = list(map(float,input().split()))
m = list(map(float,input().split()))
w = list(map(float,input().split()))
problem = 0
a2 = [-1,-1]
a2[0] = a[0] + v[0]
a2[1] = v[1] + a[1]
bord = 0
m2 = [-1,-1]
m2[0] = m[0] + v[0]
m2[1] = m[1] + v[1]
if a[0] == 0:
    if (m2[0] < v[0] and w[0] < v[0]) or (m2[0] > v[0] and w[0] > v[0]):
        sign = -1
    else:
        sign = 1
else:
    # 1 Step ищем сторону мачты
    y_ot_m = ((a2[1] - v[1])*m[0] - v[0]*a2[1] + v[1]*a2[0])/ (a2[0]- v[0])
    if y_ot_m > m[1]:
        board_m = 1
    else:
        board_m = -1
    if a[0] > 0:
        board_m = board_m * -1
    # 2 Step ищем сторону врага
    y_ot_m = ((a2[1] - v[1])*w[0] - v[0]*a2[1] + v[1]*a2[0])/ (a2[0]- v[0])
    if y_ot_m > w[1]:
        board_w = 1
    else:
        board_w = -1
    if a[0] > 0:
        board_w = board_w * -1
    if board_m == board_w:
        sign = -1
    else:
        sign = 1
# Находим угол мачты
if m2[0] == v[0] and m2[1] == v[1]:
    angle_m = 0
else:
    angle_m = acos(1/(sqrt(m[0]**2 + m[1]**2 + 1)))
    angle_m = angle_m*sign*180/pi
w[0] = w[0] - v[0]
w[1] = w[1] - v[1]
angle_w = acos((w[0]*a[0] +w[1]*a[1])/(sqrt(w[0]**2 + w[1]**2)*sqrt(a[0]**2 + a[1]**2)))
angle_w = 90 - angle_w*180/pi
if abs(angle_m) <= 60 and abs(angle_w) <= 60:
    print(board_w)
    print(round(angle_w,2))
    print(round(angle_m,2))
    print("PLS")
else:
    print(0)







