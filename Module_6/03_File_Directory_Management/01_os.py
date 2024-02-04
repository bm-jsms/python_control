from modules.divider import divider as d
import os

if os.path.exists(".gitignore"):
    print("File exists")
else:
    print("File does not exist")


d()


if os.path.exists("Module_6/03_File_Directory_Management/src"):
    print("Directory exists")
else:
    # os.makedirs("Module_6/03_File_Directory_Management/src")
    os.mkdir("Module_6/03_File_Directory_Management/src")


d()


print("[+] List files in current directory:")
resources = os.listdir()
for resource in resources:
    print(f"\t{resource}")
