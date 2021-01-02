f = open('C:/Users/nikol_000/Desktop/random/text2.txt')

n = int(f.readline())
t = []
mulm = 0


for i in range (n):
    a = int(f.readline())
    if a%7 == 0 or a%2 == 0 or a == max(t):
        t.append(a)
    j = len(t)-1
    while j!=0:
        mul = t[j]*t[j-1]
        print(mul)
        if mul>mulm and mul%14 == 0:
                mulm = mul     
        j-=1
print(mulm)
f.close()
