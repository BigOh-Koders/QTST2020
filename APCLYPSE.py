for _ in range(int(input())):
    R, C = map(int, input().split())
    R -= 1
    C -= 1
    x, y = map(int, input().split())
    days1 = abs(0 - x) + abs(0 - y)  # from corner 0,0
    days2 = abs(0 - x) + abs(C - y)  # from corner 0,C
    days3 = abs(R - x) + abs(0 - y)  # from corner R,0
    days4 = abs(R - x) + abs(C - y)  # from corner R,C
    print(max(days1, days2, days3, days4))
