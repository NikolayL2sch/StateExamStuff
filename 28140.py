f = open('C:/Users/nikol_000/Desktop/random/28140.txt')

s,n = map(int,(f.readline()).split())
t = []
ans = []


for i in range (n):
    t.append(int(f.readline()))
while sum(ans)+min(t)<=s:
    ans.append(min(t))
    t.remove(min(t))
k = s - sum(ans) + max (ans)
rmin = 10e9
for e in t:
    if e<=k and k-e<rmin:
        rmin = k-e
print(len(ans),k-rmin)

f.close()
