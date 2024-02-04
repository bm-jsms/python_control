from modules.divider import divider as d
import re


d()


text = "Today its 2020/01/01, and tomorrow it will be 2020/01/02."

matches = re.findall("\d{4}\/\d{2}\/\d{2}", text)
print(matches)


d()


text2 = "Users can contact us at support@email.io or at info@email.io."
matches2 = re.findall("(\w+)@(email.\w{2,})", text2)
print(matches2)
