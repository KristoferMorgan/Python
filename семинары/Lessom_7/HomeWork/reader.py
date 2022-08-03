from pathlib import Path

def reader(path:str,filename:str) -> list:
    filepath = Path(path,filename)
    with open (filepath,"r") as file:
        return file.readlines()