for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    distance = y - x - 2
    if distance == 0:
        print(2)
    elif distance == -1:
        print(1)
    else:
        d = dict()
        first = distance // 2
        nam = distance % 2
        d[first] = 2
        if first == 0:
            print(3)
            continue
        if first == 1:
            first = 2
            d.clear()
            d[2] = 1
        first2 = first
        isOne = False
        while True:
            if nam == 0 or first2 == 0 or isOne:
                isOne = False
                if 2 < first2:
                    print(d)
                    d.clear()
                    first -= 1
                    first2 = first
                    nam = distance % first2
                    d[first2] = distance // first2
                else:
                    print(sum(d.values()) + 2, d)
                    break
            else:
                first2 -= 1
                d[first2] = nam // first2
                if nam // first2 == 0:
                    isOne = True
                nam %= first2