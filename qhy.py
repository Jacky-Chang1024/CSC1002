import random
a = []
xx = [0, 0, -1, 1]
yy = [-1, 1, 0, 0]
direction = ['left', 'right', 'up', 'down']
direct = ['', '', '', '']
print("Welcome to Kinley’s puzzle game!")
while 1:
    print("Enter the desired dimension of the puzzle:")
    n = int(input())
    if n < 2 or n > 10:
        print("invalid!")
    else:
        break
print("Enter the four letters used for left, right, up and down directions")
direct = input().split()
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(0)
cnt = 0; up = n * n - 1; nx = 0; ny = 0;
def printnow ():
    for i in range(n):  
        for j in range(n):
            print(a[i][j], end = " ")
        print()

b = []
up = n * n
for i in range(up):
    b.append(i)
def rand_matrix ():
    flag = 1
    global nx, ny
    while flag:
        random.shuffle(b)
        now = 0
        for i in range(up):
            for j in range(i + 1, up):
                if b[i] > b[j] and b[i] > 0 and b[j] > 0:
                    now += 1
        for i in range(up):
            if b[i] == 0:
                nx = int(i / n); ny = int(i % n); break
        if (n % 2 == 1 and now % 2 == 0 or n % 2 == 0 and (now + n - nx) % 2 == 1):
            flag = 0
    global cnt
    for i in  range(n):
        for j in range(n):
            a[i][j] = b[i * n + j]
            if (b[i * n + j] == i * n + j + 1):
                cnt += 1
rand_matrix()
tot = 0
while cnt != up - 1:
    printnow()
    print("Enter your move (", end = "")
    flag = 0
    for i in range(4):
        cx = nx + xx[i]; cy = ny + yy[i]
        if cx < n and cy < n and cx >= 0 and cy >= 0:
            if not flag:
                print(direction[i]+'-'+direct[i], end = "")
                flag = 1
            else:
                print(', '+direction[i]+'-'+direct[i], end = "")
    print(")")
    flag = 0; ch = input(); cx = 0; cy = 0
    for i in range(4):
        if (ch == direct[i]):
            cx = nx + xx[i]; cy = ny + yy[i]
            if cx < n and cy < n and cx >= 0 and cy >= 0:
                flag = 1; break
    if flag:
        tot += 1
        if a[cx][cy] == cx * n + cy + 1:
            cnt -= 1
        a[nx][ny] = a[cx][cy]; a[cx][cy] = 0
        if a[nx][ny] == nx * n + ny + 1:
            cnt += 1
        nx = cx; ny = cy
    else:
        print("invalid!")
print("Congratulations! You solved the puzzle in %d moves" % tot)