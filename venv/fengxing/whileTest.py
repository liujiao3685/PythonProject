
num=24

for i in range(3):
    n=int(input('输入数字：'))
    if(n>num):
        print('old')
    elif(n<num):
        print('small')
    else:
        print('ok')
        break
else:
    print('次数用尽！')

