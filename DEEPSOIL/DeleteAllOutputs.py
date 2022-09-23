import glob, os
import pathlib
import csv
from re import sub

def navigate_dir():
    main_path = pathlib.Path(__file__).parent.resolve()
    os.chdir(main_path)
    MainFolders = glob.glob('*/')
    for i in MainFolders:
        os.chdir(f'{main_path}\\{i}')
        cMainFolderPath = os.getcwd()
        SubFolders = glob.glob('*/')
        for j in SubFolders:
            # cd to the working folder
            os.chdir(f'{cMainFolderPath}\\{j}')
            
            dir_name = os.getcwd()
            test = os.listdir(dir_name)
            for item in test:
                if item.endswith(".txt") or item.endswith(".xlsx") or item.endswith("/") or item.endswith(".sp"):
                    os.remove(os.path.join(dir_name, item))

if __name__ == "__main__":
    navigate_dir()