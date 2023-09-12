
import re
import os

global directory
global old_text
directory = False
old_text = False
while True:
    try:
        start = int(input("**選擇模式**\n-輸入 1 多行文字查找替換\n-輸入 2 正則表達式替換\n-輸入任意其他數字退出\n"))
        if start == 1:
            old_text = input("請輸入需要查找的多行文字, 換行請用‘\\n’表示： ").replace("\\n", "\n")
            new_text = input("請輸入需要替換的多行文字, 換行請用‘\\n’表示： ").replace("\\n", "\n")
        elif start == 2:
            if old_text:
                memory_old = int(input("輸入 1 繼續使用上次表達式, 其他任意數字修改表達式："))
                if memory_old != 1:
                    old_text = re.compile(input("請輸入需要查找內容的正則表達式： \ntip:開頭可以加(?sm)等以修改匹配行為！\n"))
                    new_text = input("請輸入需要替換的內容，支持多行文字, 換行請用‘\\n’表示： ").replace("\\n", "\n")
            else:
                old_text = re.compile(input("請輸入需要查找內容的正則表達式： "))
                new_text = input("請輸入需要替換的內容，支持多行文字, 換行請用‘\\n’表示： ").replace("\\n", "\n")
        else:
            exit()
        while True:
            if directory:
                memory_dir = int(input("輸入 1 繼續使用上次路徑, 其他任意數字修改路徑："))
                if memory_dir == 1:
                    break
            directory = input("請輸入文件路徑：")
            if directory == "":
                print("您沒有提供路徑，已使用默認值，路徑為當前環境目錄！")
                directory = "./"
                break
            elif os.path.exists(directory)!=True:
                print("路徑不存在！請重新輸入！")
                continue
            else:
                break
    except Exception as error:
        print(f"遇到錯誤：{error}")
        continue
        
    try:
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if filename.endswith(".md"):
                    filepath = os.path.join(root, filename)
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                    content = re.sub(old_text, new_text, content)
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)
    except Exception as error:
        print(error)
        continue

    print("替換成功！")
