nums = [1, 2, 3, 4]
powers = list()
for x in nums:
    powers.append(x * x)
else:
    print(powers)

# 列表推导式
n2 = [2, 3, 4, 5, 6]
p2 = [x * x for x in n2]
print('列表推导式:', p2)
