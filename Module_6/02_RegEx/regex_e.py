from modules.divider import divider as d
import re


d()


text = "My dog its on the floor, and my cat is on the couch."
new = re.sub("cat", "dog", text)
print(new)


d()


text2 = "Daniel,Marcos,James"
new2 = re.split(",", text2)
print(new2)
print(new2[0])
