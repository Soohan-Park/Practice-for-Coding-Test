# 어렵다.. 에라토스테네스의 채는 어떻게 쓰는건지.. 잠시 보류

import math
while True:
    target = int(input())
    if target == 0: break
    else:
        count = 0
        for t in range(target + 1, 2 * target + 1):
            # t 에 대해 소수 판별 알고리즘
            flag = True
            # 에라토스테네스의 체를 쓰면 된다고 함.. 한번 해보기
            for p in range(2, int(math.sqrt(t) + 1)):
                if t % p == 0 :
                    flag = False
                    break
            if flag: count += 1
        print(count)