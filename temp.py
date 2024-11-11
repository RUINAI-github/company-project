import math
arr = [1,2,3,4,2,1]
c =10
answer = []
n = math.log2(c)
print(n)
if n % 2 != 0:
    n = int(n) + 1
answer = arr.copy()
for i in range(2**n - c):
    answer.append(0)
print(answer)


print(math.log2(1))