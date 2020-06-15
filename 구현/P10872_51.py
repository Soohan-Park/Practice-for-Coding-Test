# Solved. (Caution! >> 0! = 1)
a = lambda x : 1 if x <= 1 else x * a(x-1)
print(a(int(input())))