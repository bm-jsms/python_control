# close the file after writing automatically using with statement
with open("Module_5/02_Read_Write/00_Hello.txt", "w") as f:
    f.write("Hello World from other side")
    f.write("\nHello World 2 from other side")


with open("Module_5/02_Read_Write/00_Hello.txt", "r") as f:
    file_content = f.read()

print(file_content)
""" Output: Hello World from other side
            Hello World 2 from other side
"""

print("*" * 25)

with open("Module_5/02_Read_Write/00_Hello.txt", "r") as f:
    for line in f:
        print(line.strip())
