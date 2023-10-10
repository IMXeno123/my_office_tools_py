import json
from assets.logs import creat_log
from pathlib import Path


class MySqlDatabases():
    def __init__(self, filepath):
        self.filepath = filepath
    
    def all_data(self):
        with open(f"{self.filepath}/config/config.ini", mode="r", encoding="UTF-8") as f:
            setting_data_1 = f.read()
        self.settings_data = json.loads(setting_data_1)
        return self.settings_data
    
    def insert_data(self, setting_data:dict):
        with open(f"{self.filepath}/config/config.ini", mode="r", encoding="UTF-8") as f:
            self.data:list = json.loads(f.read())
            if type(setting_data) == dict:
                self.data.append(setting_data)
                with open(f"{self.filepath}/config/config.ini", mode="w", encoding="UTF-8") as file:
                    json.dump(self.data, file)
            else:
                creat_log("[error] No data!")
                
    def creat_settings(self):
        if not Path(f"{self.filepath}/config/config.ini").exists():
            Path(f"{self.filepath}/config/").mkdir()
            default_path = [{"path":f"{self.filepath}"}]
            with open(f"{self.filepath}/config/config.ini", mode="w", encoding="UTF-8") as f:
                json.dump(default_path, f)
                
    def change_settings(self, setting_data:list, new_data, index:int, key_):
        setting_data[index][key_] = new_data
        with open(f"{self.filepath}/config/config.ini", mode="w", encoding="UTF-8") as file:
            json.dump(setting_data, file)
    

if __name__ == "__main__":
    my_db = MySqlDatabases()