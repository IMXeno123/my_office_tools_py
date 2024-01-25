while True:
    num = int(input('请输入一个两位整数'))
    if num >= 10 and num < 100:
        a = str(num)
        print(int(a[0])+int(a[1]))
    else:
        print('请输入正确的2位正整数')