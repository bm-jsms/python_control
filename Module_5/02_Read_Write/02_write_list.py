my_list = ["firlst line\n", "second line\n", "third line\n"]

with open("Module_5/02_Read_Write/00_Hello.txt", "w") as f:
    f.writelines(my_list)
