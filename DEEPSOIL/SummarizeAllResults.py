import glob, os
import pathlib
import csv
from re import sub

def join_results(wr):

    # Move "-EL.sp" files to unused folder
    file_path = os.getcwd()
    if not os.path.exists("./unused"):
        os.makedirs("./unused")
    for file in glob.glob("*-EL.sp"):
        os.rename(f"{file_path}\\{file}", f"{file_path}\\unused\\{file}")

    SP_All = []
    for file in glob.glob("*.sp"):
        with open(file) as f:
            lines = f.read().splitlines()
            SP_All.append(lines)
    SP_All_transpose = zip(*SP_All)

    for row in SP_All_transpose:
        wr.writerow(row)

    # Move "-EL.sp" files back to original dir
    os.chdir('./unused')
    for file in glob.glob("*-EL.sp"):
        os.rename(f"{file_path}/unused/{file}",f"{file_path}\\{file}")

def navigate_dir():
    main_path = pathlib.Path(__file__).parent.resolve()
    os.chdir(main_path)
    MainFolders = glob.glob('*/')
    myfile = open('Summary of All RS Outputs.csv', 'w', newline='')
    wr = csv.writer(myfile)

    for i in MainFolders:
        myfile.write(str(i))
        myfile.write('\n')
        os.chdir(f'{main_path}\\{i}')
        cMainFolderPath = os.getcwd()
        SubFolders = glob.glob('*/')
        for j in SubFolders:
            os.chdir(f'{cMainFolderPath}\\{j}')# cd to the working folder
            file_path = os.getcwd()
            myfile.write(str(file_path))
            myfile.write('\n')
            join_results(wr)
    myfile.close()


if __name__ == "__main__":
    navigate_dir()
