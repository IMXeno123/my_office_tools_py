import re
from pathlib import Path
from logs import creat_log

def subByDir(old_text:str, new_text:str, path:str, log_path:str|bool=False):
    """
    Need import re and os modules!
    Only support txt md.
    """
    isMatch = 0
    counts = 0
    old_text = re.compile(old_text)
    
    for root, dirs, files in Path(path).walk():
        for filename in files:
            if filename.endswith(".md") or filename.endswith(".txt"):
                filepath = Path(root) / filename
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                if re.search(old_text, content):
                    isMatch = 1
                    # log
                    if log_path:
                        creat_log(f"[info] \"{filepath}\"", log_path)
                    counts += 1
                    contents = re.sub(old_text, new_text, content)
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(contents)

    if isMatch:
        # log
        if log_path:
            creat_log(f"[info] 有{counts}個檔案替換成功!", log_path)
        isMatch = 0
        return True
    else:
        # log
        if log_path:
            creat_log(f"[info] **未匹配到內容**", log_path)
        return False
        
if __name__ == "__main__":
    ot = input("ot: ")
    ot = f"(?sm){ot}"
    nt = input("nt: ")
    dir_ = "E:/3D Objects/testfolder"
    subByDir(ot,nt,dir_)                