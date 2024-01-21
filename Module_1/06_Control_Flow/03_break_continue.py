from modules.divider import divider

for i in range(10):
    print(i)
    if i == 5:
        break


divider()


for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
