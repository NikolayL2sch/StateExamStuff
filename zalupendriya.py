n,m = map(int,input().split())
s = m
a = []
cnt = 0
for i in range (n):
    x = int(input())
    if 200<=x<=210:
        m-=x
        cnt+=1
    else:
        a.append(x)
a = sorted(a)
for i in range (len(a)):
    if m-a[i]>=0:
        m-=a[i]
        cnt+=1
        ind = i
    else:
        break
tmp = 10e9
while m+a[ind]>= a[ind+1] and tmp!=ind+1:
    for i in range (ind+1,len(a)):
        if a[i] <= m+a[ind]:
            mx = a[i]
            tmp = i
    m-= mx-a[ind]
    ind-=1
print(cnt,s-m) 
