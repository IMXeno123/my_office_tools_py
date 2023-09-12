
import re
import os

old_text = """sdaf"""
new_text = """jjj
bbb
ccc"""


directory = "E:/Downloads/pics/md"


for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            content = re.sub(old_text, new_text, content, flags=re.DOTALL)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

print("成功！")
