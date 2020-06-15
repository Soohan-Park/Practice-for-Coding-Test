# solved.
# Golf code: print("FFFFFFDCBA"[int(input())//10])

score = int(input())

score = (score // 10) - 5

scoreBoard = ["F", "D", "C", "B", "A"]

if score < 0: score = 0
elif 5 <= score: score = 4

print(scoreBoard[score])
