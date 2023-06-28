import os
filename, file_extension = os.path.splitext ('/path/to/somefile.ext')
print (filename) # '/path/to/somefile'
print (file_extension) # '.ext'

# 选择Python解释器
# 选择“查看”>“命令面板”。
# 在命令面板中，键入并选择“Python：选择解释器”。
# 在列表中选择一个Python解释器。

# 运行Python代码
# 在Visual Studio Code中打开一个Python文件。
# 选择“查看”>“终端”。
# 在终端中，键入python <file name>并按Enter键。

# 处理文件
import shutil
shutil.copy ('source.txt', 'destination.txt') # 复制文件
shutil.move ('source.txt', 'destination.txt') # 移动文件

# 处理文本
import re
text = 'Hello, world!'
pattern = re.compile ('world')
match = pattern.search (text) # 查找匹配的文本
print (match.group ()) # 'world'

# 处理网络
import requests
response = requests.get ('https://www.bing.com') # 发送GET请求
print (response.status_code) # 200
print (response.text) # 响应内容

def suffix_NameCheck (inFile):
  if os.path.splitext (inFile) [1] is None:
    raise TypeError ('\"%s\" has not a suffix' % inFile)
  else:
    return inFile

# 测试代码
print (suffix_NameCheck ('somefile.txt')) # 'somefile.txt'
print (suffix_NameCheck ('somefile')) # 抛出TypeError异常

str = 'Hello, world!'
suffix = 'world!'
result = str.endswith (suffix) # 检查字符串是否以后缀结尾
print (result) # True
