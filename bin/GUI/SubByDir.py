import re
import os


def subByDir(self, old_text:str, new_text:str, path:str):
    """
    Need import re and os modules!
    Only support txt md.
    """
    # try:       
        # sub context
    isMatch = 0
    counts = 0
    # old_text = re.compile(old_text)
    for root, dirs, files in os.walk(self.path_var.get()):
        # print(root)
        # print(dirs)
        # print(files)
        # break
        for filename in files:
            if filename.endswith(".md") or filename.endswith(".txt"):
                # Path.joinpath()
                filepath = os.path.join(root, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                if re.search(old_text, content, flags=re.M|re.S):
                    isMatch = 1
                    # log
                    self.loger_(f"[info] \"{filepath}\"", path)
                    counts += 1
                    contents = re.sub(old_text, new_text, content, flags=re.M|re.S)
                    with open(filepath, "w", encoding="utf-8") as f:
                        print(filepath)
                        print(contents)
                        f.write(contents)
                        print("YES!!!")
    if isMatch:
        # log
        log = f"[info] 有{counts}個檔案替換成功!"
        isMatch = 0
        return log
    else:
        # log
        log = f"[info] **未匹配到內容**"
        return log
                
    # except Exception as error:
    #     # log
    #     self.loger_(f"[error] 遇到錯誤：{error}", env_path)
