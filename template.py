import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep", #for deployment and CI/CD files, gitkeep file to put something in folder, folder cant be empty
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml", #ml ops tool (dvc)
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for filepath in list_of_files:
    filepath=Path(filepath)  #Path will convert forward slash to backwar slash in linux terminal or windows path
    filedir, filename = os.path.split(filepath) #split filepath and directory 


    if filedir !="": #if dir name not empty,
        os.makedirs(filedir, exist_ok=True) #make directory 
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #if file is empty or not file exits
        with open(filepath, "w") as f: #just create a file here
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")