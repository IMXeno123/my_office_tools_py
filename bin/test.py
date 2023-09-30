x = "xx"
locals()[x] = 4 # 或者 globals()[x] = 4
print(x) # 输出 x
print(xx)
print(locals()[x]) # 输出 4
