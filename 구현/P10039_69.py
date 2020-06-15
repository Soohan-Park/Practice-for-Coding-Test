# Solved.
# Caution! The answer type is Integer.
ans = 0

for i in range(5):
    score = int(input())
    if score < 40: ans += 40
    else: ans += score

print(ans//5)