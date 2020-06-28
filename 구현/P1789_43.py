# Solved.

S = int(input())
count = 0
tempSum = 0
i = 0

while tempSum < S:
    i += 1
    tempSum += i
    if tempSum <= S: count += 1

print(count)
