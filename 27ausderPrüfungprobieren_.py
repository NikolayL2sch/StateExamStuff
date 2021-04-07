t = []
m = 0
s = '0'
n = int(input())
for i in range (n):
    t.append(int(input()))
for i in range (n):
    for j in range (n):
        if i!=j and abs(t[i]-t[j])%2 == 0 and (t[i] % 11 == 0 or t[j] % 11 == 0):
            if t[i]*t[j] > m:
                m = t[i]*t[j]
                s = str(min(t[j],t[i]))+str(max(t[j],t[i]))
print(s,m)
