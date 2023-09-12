
import re
import os

old_text = """sdaf"""
new_text = """jjj
bbb
ccc"""

# 定义要搜索修改的目录
directory = "E:/Downloads/pics/md"

# 用os.walk函数，遍历目录下的所有子目录和文件
for root, dirs, files in os.walk(directory):
    # 遍历每个文件名
    for filename in files:
        # 检查文件名是否以.md结尾，如果是，就是md文件
        if filename.endswith(".md"):
            # 拼接完整的文件路径
            filepath = os.path.join(root, filename)
            # 打开文件，读取内容
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            # 用re.sub函数，把内容中的原始多行文字替换成目标多行文字，注意使用re.DOTALL标志，让.匹配换行符
            content = re.sub(old_text, new_text, content, flags=re.DOTALL)
            # 重新打开文件，写入替换后的内容
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

print("成功！")
