import json
from logs import creat_log
from pathlib import Path
from mainGui import mainGui 


class MySqlDatabases():
    def __init__(self, filepath):
        self.filepath = filepath
        with open(f"{self.filepath}/config/config.ini", mode="r", encoding="UTF-8") as f:
            text_1 = f.read()
        self.users = json.loads(text_1)
    
    def all_data(self):
        with open(f"{self.filepath}/config/config.ini", mode="r", encoding="UTF-8") as f:
            text_2 = f.read()
        self.settings_data = json.loads(text_2)
        return self.settings_data
    
    def insert_data(self, setting_data:dict):
        with open(f"{self.filepath}/config/config.ini", mode="r", encoding="UTF-8") as f:
            self.data:list = json.loads(f.read())
            if type(setting_data) == dict:
                self.data.append(setting_data)
                with open(f"{self.filepath}/config/config.ini", mode="w", encoding="UTF-8") as file:
                    json.dump(self.data, file)
            else:
                mainGui().loger_("[error] No data!")
                
    def creat_settings(self, path):
        if not Path(f"{self.filepath}/config/config.ini").exists():
            Path(f"{self.filepath}/config/").mkdir()
            default_path = {"path":path}
            with open(f"{self.filepath}/config/config.ini", mode="w", encoding="UTF-8") as f:
                json.dump(default_path, f)
                
    def get_settings(self):
        pass
    

if __name__ == "__main__":
    my_db = MySqlDatabases()
    my_db.check_login("jason","123456")
    print(my_db.all_data())
    my_db.get_data({"D":1})