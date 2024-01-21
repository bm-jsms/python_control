my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for element in my_list:
    print(f"\n[+] Nested loop for {element}")
    for nested_element in element:
        print(nested_element)
