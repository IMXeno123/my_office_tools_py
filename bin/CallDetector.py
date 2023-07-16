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
        print("Hi! I'm an umbrella.")
    i = 1
    weather = str.upper(input("Is it raining outside right now?\nType 'T'or'F: "))
    if weather == "T":
        print("Your choice is T. So it's raining!")
        return True
    elif weather == "F":
        print("Your choice is F. So it's not raining! Bye!")
        return False
    else:
        print("ummmm... Only support T or F!!!")
        return "exit"

while True:
    re = umbrella()
    if re == "exit":
        break
    print(re,"\n--------------------------------")
