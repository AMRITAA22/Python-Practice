N=2
area=[]
for i in range(N):
    x,y=map(int,input().split())
    val=x*y/2
    area.append(val)
max=area[0]
for i in range(len(area)):
    if max<area[i]:
        max=area[i]
print(max)
