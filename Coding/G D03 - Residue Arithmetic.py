n, m = map(int,input().split())
a1, a2 = map(int,input().split())
b1, b2 = map(int,input().split())
c1, c2 = map(int,input().split())


while(a1!=a2):
    if(a1<a2):
        a1=a1+n
    else:
        a2=a2+m
a = a1
while(b1!=b2):
    if(b1<b2):
        b1=b1+n
    else:
        b2=b2+m
b = b1


while(c1!=c2):
    if(c1<c2):
        c1=c1+n
    else:
        c2=c2+m
c = c1

print(2*a+b-c)
