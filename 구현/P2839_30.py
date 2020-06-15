# Solved.
N = int(input())

ans = None

if N == 3:
    ans = 1
else:
    times = N // 5  # N에 가까운 5의 배수부터 역으로 줄여가며 계산
    if times == 0: # 1~4(3제외)인 경우
        ans = -1
    else:
        if N % 3 == 0: # 3의 배수인 경우, 일단 N//3으로 잡아둔다. 이후 반복문에서 값이 나오게 된다면, 그 값은 항상 N//3보다 작기 때문.
            ans = N // 3

        for t in range(times,0,-1): # 5t, 5(t-1), ... , 5
            rest = N - (5 * t) # (11 % 10 == 1) & (11 % 5 == 1) 방지를 위해
            if rest % 3 == 0:
                ans = t + (rest // 3) # t: 5kg || rest//3: 3kg
                break

        if ans is None: # 위의 모든 경우의 수에 포함되지 않을 경우, ans is None
            ans = -1

print(ans)