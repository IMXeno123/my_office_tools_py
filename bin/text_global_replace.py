import re
import os

def sub_by_dir(directory:str = False, old_text:str = False, new_text:str = False, isMemory:int = 1):
    """
    Need import re and os modules!
    Only support txt md.
    """
    try:
        isReset = 0
        while True:
            mode = input("**選擇模式**\n-輸入 1 多行文字查找替換\n-輸入 2 正則表達式替換\n-輸入任意其他數字退出\n")
            # mode 1
            if mode == "1":
                while True:
                    # Memory of old_text
                    while True:
                        if isMemory == 1:
                            if old_text:
                                choices_ = input("按 enter 使用已有的 查找 多行文字\n輸入 0 重新選擇模式\n輸入其他任意字符串修改 查找 多行文字\n")
                                if choices_ == "":
                                    break
                                elif choices_ == "0":
                                    isReset = 1
                                    break
                                else:
                                    old_text = False
                                    continue
                            else:
                                old_text = input("請輸入需要 查找 的多行文字, 換行符請用‘\\n’表示:\n").replace("\\n", "\n")
                                if old_text != "":
                                    break
                                else:
                                    old_text = False
                                    print("**未輸入內容**")
                                    continue
                        else:
                            old_text = input("請輸入需要 查找 的多行文字, 換行符請用‘\\n’表示:\n").replace("\\n", "\n")
                            if old_text != "":
                                break
                            else:
                                old_text = False
                                print("**未輸入內容**")
                                continue
                    if isReset:
                        old_text = False
                        new_text = False
                        isReset = 0
                        break
                    # Memory of new_text
                    while True:
                        if isMemory == 1:
                            if new_text:
                                choices_ = input("按 enter 使用已有的 替換 多行文字\n輸入 0 重新選擇模式\n輸入其他任意字符串修改 替換 多行文字\n")
                                if choices_ == "":
                                    break
                                elif choices_ == "0":
                                    isReset = 1
                                    break
                                else:
                                    new_text = False
                                    continue
                            else:
                                new_text = input("請輸入需要 替換 的多行文字, 換行請用‘\\n’表示： \n").replace("\\n", "\n")
                                break
                                # if new_text != "":
                                #     break
                                # else:
                                #     new_text = False
                                #     print("**未輸入內容**")
                                #     continue
                        else:
                            new_text = input("請輸入需要 替換 的多行文字, 換行請用‘\\n’表示： \n").replace("\\n", "\n")
                            break
                            # if new_text != "":
                            #     break
                            # else:
                            #     new_text = False
                            #     print("**未輸入內容**")
                            #     continue
                    if isReset:
                        old_text = False
                        new_text = False
                        isReset = 0
                        break
                    # Memory of directory
                    while True:
                        if isMemory == 1:
                            if directory:
                                choices_ = input("按 enter 使用已有的路徑\n輸入 0 重新選擇模式\n輸入其他任意字符串修改路徑\n")
                                if choices_ == "":
                                    break
                                elif choices_ == "0":
                                    isReset = 1
                                    break
                                else:
                                    directory = False
                                    continue
                            else:
                                directory = input("請輸入 路徑\n")
                                if os.path.exists(directory)!=True:
                                    print("**路徑不存在**")
                                    directory = False
                                    continue
                                else:
                                    break         
                        else:
                            directory = input("請輸入 路徑\n")
                            if os.path.exists(directory)!=True:
                                print("**路徑不存在**")
                                directory = False
                                continue
                            else:
                                break
                    if isReset:
                        old_text = False
                        new_text = False
                        isReset = 0
                        break
                    # sub context
                    isMatch = 0
                    counts = 0
                    for root, dirs, files in os.walk(directory):
                        for filename in files:
                            if filename.endswith(".md") or filename.endswith(".txt"):
                                filepath = os.path.join(root, filename)
                                with open(filepath, "r", encoding="utf-8") as f:
                                    content = f.read()
                                if re.search(old_text, content, flags=re.M|re.S):
                                    isMatch = 1
                                    print(filepath)
                                    counts += 1
                                    content = re.sub(old_text, new_text, content, flags=re.M|re.S)
                                    with open(filepath, "w", encoding="utf-8") as f:
                                        f.write(content)
                    if isMatch:
                        print("--------------------------------------------------")
                        print(f"有{counts}個檔案替換成功!\n--------------------------------------------------\n")
                        isMatch = 0
                    else:
                        print("**未匹配到內容**\n--------------------------------------------------\n")
            # mode 2
            elif mode == "2":
                while True:
                    # Memory of old_text
                    while True:
                        if isMemory == 1:
                            if old_text:
                                choices_ = input("按 enter 使用已有表達式\n輸入 0 重新選擇模式\n輸入其他任意字符串修改表達式\n")
                                if choices_ == "":
                                    break
                                elif choices_ == "0":
                                    isReset = 1
                                    break
                                else:
                                    old_text = False
                                    continue
                            else:
                                old_text = input("請輸入需要 查找 的正則表達式\ntip:開頭可以加(?sm)等, 以修改匹配行為!\n")
                                if old_text != "":
                                    old_text = re.compile(old_text)
                                    break
                                else:
                                    old_text = False
                                    print("**未輸入內容**")
                                    continue
                        else:
                            old_text = input("請輸入需要 查找 的正則表達式\ntip:開頭可以加(?sm)等, 以修改匹配行為!\n")
                            if old_text != "":
                                old_text = re.compile(old_text)
                                break
                            else:
                                old_text = False
                                print("**未輸入內容**")
                                continue
                    if isReset:
                        old_text = False
                        new_text = False
                        isReset = 0
                        break
                    # Memory of new_text
                    while True:
                        if isMemory == 1:
                            if new_text:
                                choices_ = input("按 enter 使用已有的 替換 多行文字\n輸入 0 重新選擇模式\n輸入其他任意字符串修改 替換 多行文字\n")
                                if choices_ == "":
                                    break
                                elif choices_ == "0":
                                    isReset = 1
                                    break
                                else:
                                    new_text = False
                                    continue
                            else:
                                new_text = input("請輸入需要 替換 的多行文字, 換行請用‘\\n’表示： \n").replace("\\n", "\n")
                                break
                                # if new_text != "":
                                #     break
                                # else:
                                #     new_text = False
                                #     print("**未輸入內容**")
                                #     continue
                        else:
                            new_text = input("請輸入需要 替換 的多行文字, 換行請用‘\\n’表示： \n").replace("\\n", "\n")
                            break
                            # if new_text != "":
                            #     break
                            # else:
                            #     new_text = False
                            #     print("**未輸入內容**")
                            #     continue
                    if isReset:
                        old_text = False
                        new_text = False
                        isReset = 0
                        break
                    # Memory of directory
                    while True:
                        if isMemory == 1:
                            if directory:
                                choices_ = input("按 enter 使用已有的路徑\n輸入 0 重新選擇模式\n輸入其他任意字符串修改路徑\n")
                                if choices_ == "":
                                    break
                                elif choices_ == "0":
                                    isReset = 1
                                    break
                                else:
                                    directory = False
                                    continue
                            else:
                                directory = input("請輸入 路徑\n")
                                if os.path.exists(directory)!=True:
                                    print("**路徑不存在**")
                                    directory = False
                                    continue
                                else:
                                    break         
                        else:
                            directory = input("請輸入 路徑\n")
                            if os.path.exists(directory)!=True:
                                print("**路徑不存在**")
                                directory = False
                                continue
                            else:
                                break
                    if isReset:
                        old_text = False
                        new_text = False
                        isReset = 0
                        break
                    # sub context
                    isMatch = 0
                    counts = 0
                    for root, dirs, files in os.walk(directory):
                        for filename in files:
                            if filename.endswith(".md") or filename.endswith(".txt"):
                                filepath = os.path.join(root, filename)
                                with open(filepath, "r", encoding="utf-8") as f:
                                    content = f.read()
                                if re.search(old_text, content):
                                    isMatch = 1
                                    print(filepath)
                                    counts += 1
                                    content = re.sub(old_text, new_text, content)
                                    with open(filepath, "w", encoding="utf-8") as f:
                                        f.write(content)
                    if isMatch:
                        print("--------------------------------------------------")
                        print(f"有{counts}個檔案替換成功!\n--------------------------------------------------\n")
                        isMatch = 0
                    else:
                        print("**未匹配到內容**\n--------------------------------------------------\n")
            else:
                print("--------------------------------------------------\nBye~~~")
                break
    except Exception as error:
        print(print(f"遇到錯誤：{error}"))

sub_by_dir()
