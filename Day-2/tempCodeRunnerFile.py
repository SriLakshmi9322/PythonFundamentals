x1, y1 = 5, 5
x2, y2 = 'sri', 'sri'
x3, y3 = [1, 2, 3], [1, 2, 3]

print(id(x1))           # 140723072718624
print(id(y1))           # 140723072718624
print(x1 is y1)
print(x1 is not y1)
print(id(x2))           # 140723072718624
print(id(y2))           # 140723072718624
print(x2 is y2)
print(x2 is not y2)
print(id(x3))           # 140723072718624
print(id(y3))           # 140723072718624
print(x3 is y3)
print(x3 is not y3)