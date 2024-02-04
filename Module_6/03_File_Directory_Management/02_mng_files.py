import os

if os.path.exists("text2.txt"):
    os.rename("text2.txt", "changed.txt")
