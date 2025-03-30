def team_1(N,score, over):
    for i in range(N):
        x,y=map(int,input().split())
        score+=y
        over+=x
    print('team1 core ',score,'over ',over)
    return score, over
def team_2(score,over):
    print('required run rate to chase the score : ',score/over)

N=int(input('enter the number of overs: '))
score=0
over=0

while True:
    print('enter team 1 score: ')
    print('display required run rate for team2: ')
    print('exit')
    ch=int(input('enter your choice'))
    if ch==1:
        a,b=team_1(N,score, over)
    if ch==2:
        team_2(a,b)
    if ch==3:
        break
