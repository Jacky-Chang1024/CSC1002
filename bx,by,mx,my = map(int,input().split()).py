bx,by,mx,my = map(int,input().split())

l=[[1 for i in range(by+1)] for j in range(bx+1)]
def z(mx,my,l):
    m1=[1,-1]
    m2=[2,-2]
    l[mx][my]=0
    for i in range(2):
        for j in range(2):
            if mx+m1[i] in range(bx+1) and my+m2[j] in range(by+1):
                l[mx+m1[i]][my+m2[j]] = 0
            if mx+m2[i] in range(bx+1) and my+m1[j] in range(by+1):
                l[mx+m2[i]][my+m1[j]] = 0
    return l


l=z(mx,my,l)
for i in range(bx+1):
    for j in range(by+1):
        if l[i][j]==0 :
            if i == 0 and j != by:
                l[i][j+1]=l[i][j]
            if j == 0 and i != bx:
                l[i+1][j]=l[i][j]    
            else:
                
                pass
        elif i!=0 and j != 0:
            l[i][j]=l[i-1][j]+l[i][j-1]

print(l[bx][by])