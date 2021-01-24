import time
t0 = time.time()
n = 1
k = 0
ans = []
def rec(n,k):
    global left, right #глобальные границы отрезка
    left = 34
    right = 59
    if k > 6:
        return 0
    if n > right:  # выход за границу справа
        return 0
    if left <= n <= right:  # все ок
        if k == 6 and n not in ans: # проверяем кол-во проделанных команд
            ans.append(n)  
            return 1
        else:
            return 0
    k += 1
    return rec(n+1,k)+rec(n+2,k)+rec(n*2,k)
 
print(rec(n,k))
print(*ans)
t1 = time.time() - t0
#print("Time elapsed: ", t1)