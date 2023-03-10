

x = [[4, 3, 1], [2, 1, 3], [1, 2, 4]]

print(x)

x.sort(key=lambda x: x[1])
print(x)

x.sort(key=lambda x: x[-3])
print(x)

