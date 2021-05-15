answer_board = [['W','B','W','B','W','B','W','B'], ['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'], ['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'], ['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'], ['B','W','B','W','B','W','B','W']]
def find_change(board, n):
    count = 0
    for i in range(8):
        for j in range(8):
            b = board[i][j]
            if n == 1:
                if b != answer_board[i][j]:
                    count += 1
            else:
                if b == answer_board[i][j]:
                    count += 1
    return count

y, x  = map(int, input().split())
board = [[] for _ in range(y)]
for m in range(y):
    for c in input():
        board[m].append(c)
x1 = 8
y1 = 8
answer = 2500
while True:
    b = []
    for m in range(y1 - 8, y1):
        l = []
        for n in range(x1 - 8, x1):
            l.append(board[m][n])
        b.append(l)
    a = min([find_change(b, 0),find_change(b, 1)])
    if a < answer:
        answer = a
    x1 += 1
    if x1 > x:
        x1 = 8
        y1 += 1
        if y1 > y:
            break
print(answer)