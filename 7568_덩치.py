people = []
for i in range(int(input())):
    people.append(tuple(map(int, input().split())))
for i in range(len(people)):
    count = 1
    p1 = people[i]
    for j in range(len(people)):
        p2 = people[j]
        if p1[0] < p2[0] and p1[1] < p2[1]:
            count += 1
    print(count, end=" ")