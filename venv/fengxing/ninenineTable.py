
##################  test1
for x in range(1,10):
    for y in range(1,x+1):
        print('%s * %s = %d'%(x,y,x*y),end = '  ')
    print('')

##################  test2
list1 =  [91, 95, 97, 99]
list2 =  [92, 93, 96, 98]
list3=[]

for x in list1:
    list3.append(x)

for x in list2:
    list3.append(x)

list3.sort()

print(list3)

##################  test3
# 提示：x ** y 表示 x的y次幂
def mi(x,y):
    result = x**y
    print('%s ** %s = %d'%(x,y,result))
    return  result
print(mi(2,3))
