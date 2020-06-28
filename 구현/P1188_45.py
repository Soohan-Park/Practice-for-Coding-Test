# 로직을 어떻게 잡아야 할지 감이 안오네.. 일단 맞는거 같은데 예외 케이스가 뭐가 있는지..

N, M = map(int, input().split())
# amount = round(N / M, 2) # 0.33333.... 같이 약간의 오차를 방지하기 위해 Scale을 1/100 까지로 보정.(1 <= N, M <= 100)
amount = N / M
count = 0

for i in range(N):
    mok = 1 // amount
    if amount * mok == 1:
        mok -= 1
    count += mok

print(int(count))
# print(1 / amount)
# print(1 // amount)
# print(1 % amount)

