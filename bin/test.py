functions = {}

for i in ["Exit"]:
    functions [f'function{i}'] = f'''
def function{i}():
    print("Hi")
function{i}()
'''
    
exec(functions[f"function{i}"])