for _ in range(int(input())):
    R, C = map(int, input().split())
    R -= 1
    C -= 1
    x, y = map(int, input().split())
    edge1 = abs(0 - y)  # from left edge
    edge2 = abs(0 - x)  # from top edge
    edge3 = abs(C - y)  # from right edge
    edge4 = abs(R - x)  # from bottom edge
    print(max(edge1, edge2, edge3, edge4))
