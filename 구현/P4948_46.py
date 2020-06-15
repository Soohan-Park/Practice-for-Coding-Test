# import math
# while True:
#     target = int(input())
#     if target == 0 : break
#     else:
#         count = 0
#         for t in range(target + 1, 2 * target + 1):
#             # t 에 대해 소수 판별 알고리즘
#             flag = True
#             # 에라토스테네스의 체를 쓰면 된다고 함.. 한번 해보기
#             for p in range(2, int(math.sqrt(t) + 1)):
#                 if t % p == 0 :
#                     flag = False
#                     break
#             if flag: count += 1
#         print(count)

from math import sqrt
while True:
    temp = int(input())
    if temp == 0: break
    else:
        start = temp
        end = temp * 2
        cp = int(sqrt(end))
        target = list(range(start + 1, end + 1))
        count = len(target)
        for i in range(2, cp+1):
            for j in range(len(target)):
                if target[j] is not None and target[j] % i == 0:
                    target[j] = None
                    count -= 1
        print(count)

# test = [None, 1, 2, 3, None]
# print(len(test))
# print(test.count(None))