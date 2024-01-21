first_number = 12
second_number = 7
result = first_number ** second_number

# print(first_number + second_number)
print(result)  # 35831808
print(type(result))  # <class 'int'>
print("{:,}".format(result).replace(",", "."))  # 35.831.808


odd_numbers = [1, 3, 5, 7]
even_numbers = [2, 4, 6, 8]
list_result = list(map(sum, zip(odd_numbers, even_numbers)))

print(list_result)  # [3, 7, 11, 15]
