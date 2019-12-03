# 函数允许同时全部或部分使用固定参数、默认参数、单值（一颗星）可变参数、键值对（两颗星）可变参数，使用时必须按照前述顺序书写。


def mutil_sum(*args):
    s = 0
    for x in args:
        s += x
    return s


print('mutil_sum:', mutil_sum(1, 2, 3, 4))


def dosomethings(name, age, gender='man', *codes, **classC):
    print('name：%s age:%d gender:%s ' % (name, age, gender))
    print('codes:', codes)
    print('classCode:', classC)


dosomethings('zs', 22, 'woman', 110, 60, math=90, english=120)

# more：
a = (1, 2, 3)
print(a)
print(*a)

b = [1, 2, 3]
print(b)
print(*b)

c = {'name': 'xufive', 'age': 51}
print(c)
print(*c)
print('name:{name}, age:{age}'.format(**c))
