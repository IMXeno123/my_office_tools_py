# 导入re模块，用于正则表达式匹配和替换
import re
# 导入os模块，用于操作文件和目录
import os

# 定义要替换的原始多行文字和目标多行文字
old_text = """你好吗？
我很好！"""
new_text = """你吃饭了么？

我吃了！你呢！"""

# 定义要搜索修改的目录
directory = "/user/doc/"

# 遍历目录下的所有文件名
for filename in os.listdir(directory):
    # 检查文件名是否以.md结尾，如果是，就是md文件
    if filename.endswith(".md"):
        # 拼接完整的文件路径
        filepath = os.path.join(directory, filename)
        # 打开文件，读取内容
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        # 用re.sub函数，把内容中的原始多行文字替换成目标多行文字，注意使用re.DOTALL标志，让.匹配换行符
        content = re.sub(old_text, new_text, content, flags=re.DOTALL)
        # 重新打开文件，写入替换后的内容
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

