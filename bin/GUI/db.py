import json
from logs import creat_log
from pathlib import Path


class MySqlDatabases():
    def __init__(self, filepath):
        self.filepath = filepath
        with open(f"{self.filepath}/users.json", mode="r", encoding="UTF-8") as f:
            text_1 = f.read()
        self.users = json.loads(text_1)
    
    def check_login(self, username:str, password:str):
        for user in self.users:
            if username == user["username"] and password == user["password"]:
                return (True, creat_log("[info] Succeeded"))
        return (False, creat_log("[warning] Failed"))

    def all_data(self):
        with open(f"{self.filepath}/students.json", mode="r", encoding="UTF-8") as f:
            text_2 = f.read()
        self.students = json.loads(text_2)
        return self.students
    
    def insert_data(self, student:dict):
        with open(f"{self.filepath}/students.json", mode="r", encoding="UTF-8") as f:
            self.data:list = json.loads(f.read())
            if type(student) == dict:
                self.data.append(student)
                with open(f"{self.filepath}/students.json", mode="w", encoding="UTF-8") as file:
                    json.dump(self.data, file)
            else:
                creat_log("[error] No data!")
        
PATH = Path(__file__).parent      
my_db = MySqlDatabases(PATH)
if __name__ == "__main__":
    my_db = MySqlDatabases()
    my_db.check_login("jason","123456")
    print(my_db.all_data())
    my_db.get_data({"D":1})