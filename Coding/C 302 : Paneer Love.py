n = int(input())
ai = []
pi = []
cost = 0

for i in range(n):
    x,y = map(int,input().split())
    ai.append(x)
    pi.append(y)

for i in range(0,len(pi)-1):
    if(pi[i]<pi[i+1]):
        pi[i+1] = pi[i]
        
for i in range(n):
    cost+=ai[i]*pi[i]
    
print(cost)
