from modules.divider import divider as d
import os


d()


path = os.getcwd()
print(path)


d()


files = os.listdir(path)
print("[*] Files in the current directory:")
for file in files:
    print(f"\t- {file}")
