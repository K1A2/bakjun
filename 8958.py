for _ in range(int(input())):
    ox = input()
    count_o = 0
    socre = 0
    for i in ox:
        if i == "O":
            count_o += 1
            socre += count_o
        else:
            count_o = 0
    print(socre)