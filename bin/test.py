﻿# while True:
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

# while True:
#     num = input('请输入一个两位正整数')
#     if int(num) >= 10 and int(num) < 100 and len(num) == 2:
#         b = 0
#         for i in range(len(num)):
#             b += int(num[i])
#         print(b)
#     else:
#         print("请输入正确的两位正整数")

# while True:
#     num1 = int(input('请输入第一个整数'))
#     num2 = int(input('请输入第一个整数'))
#     if num1 < num2:
#         sum = 0
#         for i in range(num1,num2+1):
#             sum += i
#             print(sum)
        
#     else:
#         print('NO')

# a=int(input())
# b=int(input())
# if a<b:
#     sum=0
#     print(list(range(a,b+1)))
#     for i in range(a,b+1):
#         sum+=i
#     print(sum)
# else:
#     print("NO")

# import turtle as tt
# pen1 = tt.Pen()
# pen1.pensize(5)
# pen1.pencolor("red")
# for i in range(5):
#     pen1.forward(100)
#     pen1.right(144)
# pen1.hideturtle()
# tt.done()

# print('会当凌绝顶')

# #指示变量，监督回答是否正确
# score = 0

# #重复问 5 次
# for i in range(5):
    
#     poem = input('请输入下一句：')
    
#     #如果答案正确，显示正确，指示变量 score 变为 1，退出循环
#     if poem == '一览众山小':
        
#         print('正确')
#         score = 1
#         break
#     else:
#         print('错误')
        
# #如果指示变量在循环后没有变化，说明一次也没有答对
# if score == 0:
    
#     print('请你再接再厉')
    

# sentence = input()
# #建立一个空字符串用来存储反过来的字符串
# sentence2 = ''
# #2个字符以及一下的数据不算回文
# if len(sentence) > 2:
#     #将字符串从后到前加到空字符串里
#     for i in range(len(sentence)-1, -1, -1):
#         sentence2 += sentence[i]
#     if sentence2 == sentence:
#         print(1)
#     else:
#         print(0)
# else:
#     print('不够长')

# import turtle as tt
# pen1 = tt.Pen()
# color_list = ['red', 'orange', 'yellow', 'green', 
#               'cyan', 'blue', 'purple', 'Magenta']
# pen1.pensize(10)
# for i in range(8):
#     pen1.pencolor(color_list[i])
#     for j in range():
#         j += 1
#         pen1.pensize(j)
#         pen1.forward(j*10)
#         pen1.right(90)
#         pen1.forward(j*10)
#         pen1.right(180-45)
#         pen1.goto(0,0)
#         pen1.right(45*3)
#     pen1.right(45)
# pen1.hideturtle()
# tt.done()


# #海龟画图
# import turtle
# t = turtle.Pen()
# #储存颜色列表
# colorlist = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple', 'Magenta']
# #每层递进
# for j in range(10,101,10):
#     #每层8瓣风车叶片
#     for i in range(8):
#         #使用轮换的颜色
#         t.pencolor(colorlist[i%8])
#         #使用和本层相关的画笔粗细
#         t.pensize(j//10)
#         t.forward(j)
#         t.right(90)
#         t.forward(j)
#         t.goto(0,0)
#         #一片叶子45度
#         t.left(45)
# #隐藏画笔
# t.hideturtle()
# turtle.done()
import turtle as tt
pen1 = tt.Pen()
colorlist = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple', 'Magenta']
pen1.pensize(10)
for i in range(8):
    pen1.pencolor(colorlist[i])
for j in range(10):
    j += 1
    pen1.forward(j)
    pen1.right(90)
    pen1.forward(j*10)
    
    