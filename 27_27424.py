f = open('text.txt')

n = int(f.readline())
t = []
s = 0

for i in range (n):
    a,b = map(int,f.readline().split)
    t.append(a)
    t.append(b)
for i in range(0,len(t)-1,2):
    s+=min(t[i],t[i+1])
if s%3!=0:
    print(s)
else:
    splm = 10e20
    for i in range(0,len(t)-1,2):
        spl = abs(t[i]-t[i+1])
        if spl<splm and (s + spl)%5!=0:
            splm = spl
    print(s-splm) 
f.close()
