# while True:
#     num = int(input('请输入一个两位正整数'))
#     if num >= 10 and num < 100:
#         a = str(num)
#         print(int(a[0])+int(a[1]))
#     else:
#         print('请输入正确的两位正整数')

# a = input("请输入一个两位正整数")
# if len(a) == 2:
#     b = 0
#     for i in range(len(a)):     #[0,1]
#         b += int(a[i])
#     print(b)
# else:
#     print("请输入正确的两位正整数")

while True:
    num = input('请输入一个两位正整数')
    if int(num) >= 10 and int(num) < 100 and len(num) == 2:
        b = 0
        for i in range(len(num)):
            b += int(num[i])
        print(b)
    else:
        print("请输入正确的两位正整数")