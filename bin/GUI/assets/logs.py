import time
from pathlib import Path


def creat_log(log, path=".."):
    # print(log)
    c_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    bool_ = Path(f"{path}/logs/").exists()
    my_log = None
    if bool_:
        with open(f"{path}/logs/log.txt", mode="a", encoding="UTF-8") as f:
            my_log = f"{c_time} {log}\n"
            f.write(my_log)
    else:
        Path(f"{path}/logs/").mkdir(parents=True)
        with open(f"{path}/logs/log.txt", mode="a", encoding="UTF-8") as f:
            my_log = f"{c_time} {log}\n"
            f.write(my_log)
    return my_log
    
def get_log(path=".."):
    bool_ = Path(f"{path}/logs/log.txt").exists()
    if bool_:
        with open(f"{path}/logs/log.txt", mode="r", encoding="UTF-8") as f:
            log_content = f.read()
            return log_content
    
if __name__ == "__main__":
    creat_log("123456, I'll go to sleep! Now")