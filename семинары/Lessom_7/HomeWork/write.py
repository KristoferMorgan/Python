from pathlib import Path

def write(field:str, path: str,filename:str )-> None:
    filepath = Path(path,filename)
    with open(filepath,"a") as file:
        file.write(field)