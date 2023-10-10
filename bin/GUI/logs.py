import time


def creat_log(log):
    # return None
    print(log)
    c_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("./log.txt", mode="a", encoding="UTF-8") as f:
        f.write(f"{c_time} {log}\n")
        
if __name__ == "__main__":
    creat_log("123456, I'll go to sleep! Now")