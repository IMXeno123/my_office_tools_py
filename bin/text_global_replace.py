from math import log
import re
import os

def sub_by_dir(directory:str = False, old_text:str = False, new_text:str = False, isMemory:int = 1):
    """
    Need import re and os modules！
    """
    try:
        while True:
            mode = input("**選擇模式**\n-輸入 1 多行文字查找替換\n-輸入 2 正則表達式替換\n-輸入任意其他數字退出\n:")
            # mode 1
            if mode == "1":
                # Memory of text
                while True:
                    if isMemory == 1:
                        if old_text:
                            memory_old = input("按 enter 繼續使用上次表達式\n輸入 0 重新選擇模式\n輸入其他任意字符串修改表達式\n：")
                            if memory_old == "":
                                break
                            elif memory_old == "0":
                                break
                            else:
                                old_text = False
                                continue
                                
                        elif isMemory == 0:
                            pass
                    else:
                        old_text = input("請輸入需要查找的多行文字, 換行符請用‘\\n’表示： \n").replace("\\n", "\n")
                        break
                
            
    except Exception as error:
        print(print(f"遇到錯誤：{error}"))



sub_by_dir()
