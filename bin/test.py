import os
path = "E:/Documents/OneDrive/Document/Note/me/01_Documents/Resouerces/Movies/81号档案/actors" # 指定文件夹路径
files = [] # 创建一个空列表用于存储所有文件
# for root, dirs, filenames in os.walk(path): # 遍历所有子目录和子目录下的子目录
#     for filename in filenames: # 遍历当前目录下的所有文件
#         files.append(f"{root}/{filename}") # 把当前目录路径和当前文件名拼接成完整路径，并添加到列表中
files = [f"{path}/{f}" for f in os.listdir(path) if os.path.isfile(f"{path}/{f}")] 
for file in files:
    if file.endswith(".md") or file.endswith(".txt"):
        print(file)
    else:
        print("bruh")