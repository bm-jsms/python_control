f = open("Module_5/02_Read_Write/00_Hello.txt", "w")
f.write("Hello World")
f.write("\nHello World 2")

f.close()
f.write("Hello World")  # This will give an error as the file is closed
