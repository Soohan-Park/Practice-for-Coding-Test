# solved.

changes = 1000 - int(input())
count = 0

while changes != 0:
    if changes >= 500:
        count += changes // 500
        changes = changes % 500
    elif changes >= 100:
        count += changes // 100
        changes = changes % 100
    elif changes >= 50:
        count += changes // 50
        changes = changes % 50
    elif changes >= 10:
        count += changes // 10
        changes = changes % 10
    elif changes >= 5:
        count += changes // 5
        changes = changes % 5
    else:
        count += changes // 1
        changes = changes % 1

print(count)
