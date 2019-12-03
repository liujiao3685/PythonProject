a = [{'name': 'zs', 'age': 15}, {'name': 'ls', 'age': 33}]

print(sorted(a, key=lambda x: x['name']))

print(sorted(a, key=lambda x: x['age']))

nums = [2, 4, 5]
for x in map(lambda i: i * i, nums):
    print(x,end=' ')
