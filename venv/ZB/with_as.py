
fp = open(r"C:\test.dat",'r')
try:
    print(fp.readline())
finally:
    fp.close()

#一行代码解决：with..as
with open(r"C:\test.dat",'r') as fp:
    print('with..as:',fp.readline())

