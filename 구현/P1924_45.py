x, y = map(int, input().split())

dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

sumDate = 0
for i in range(1, x):
    sumDate += dict[i]
sumDate += y-1

DoW = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
print(DoW[sumDate % 7])