def umbrella():
    '''
    I'm just an umbrella!!!
    '''
    global i
    try:
        a = i
    except:
        i = 0
    if i!=1:
        print("你好，我是一把智能雨伞！")
    i = 1
    weather = str.upper(input("现在外面有下雨吗？\n输入T表示有，输入F表示没有："))
    if weather == "T":
        print("你输入了T，所以表示外面有下雨，撑我吧！")
        return True
    elif weather == "F":
        print("你输入了F，所以表示外面没有下雨，不用带我出门，再见！")
        return False
    else:
        print("你在干什么啊？明明叫你输入T或F！！！")
        return "exit"

while True:
    re = umbrella()
    if re == "exit":
        break
    print(re,"\n--------------------------------")
