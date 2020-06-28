# Solved.

# Optimized.
while True:
    lines = list(map(int, input().split()))
    if 0 in lines: break

    lines.sort()
    powedLines = [ x ** 2 for x in lines ]
    print("right") if powedLines[0] + powedLines[1] == powedLines[2] else print("wrong")


# First
"""
while True:
    lines = list(map(int, input().split()))
    if 0 in lines: break

    maxLine = lines.pop(lines.index(max(lines)))
    powedMaxLine = maxLine ** 2
    powedLines = [ x ** 2 for x in lines ]
    print("right") if sum(powedLines) == powedMaxLine else print("wrong")
"""