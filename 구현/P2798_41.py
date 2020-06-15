# 틀렸습니다가 나옴. 고민 필요.

N, M = map(int, input().split())
cards = list(map(int, input().split()))

import itertools
comb = itertools.combinations(cards, 3) # 조합 생성
makeSum = lambda x : sum(next(x)) # 조합으로 생성된 튜플을 더해주는 람다식
ans = makeSum(comb) # 첫 항
try:
    while True:
        target = makeSum(comb) # 다음꺼 꺼내서
        if abs(M - target) < abs(M - ans): # M과 차이의 절대값이 작으면 ans로 대체
            ans = target
except StopIteration: # 끝에 다다르면 던져지는 예외
    pass
finally:
    print(ans) # 결과 출력