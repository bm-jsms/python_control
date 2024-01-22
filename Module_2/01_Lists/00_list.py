from modules.divider import divider


ports_tcp = [21, 22, 23, 80, 443, 69, 445]

print(ports_tcp)  # [21, 22, 23, 80, 443, 69, 445]
ports_tcp.append(8080)
print(len(ports_tcp))  # 8

ports_tcp.sort()

for port in ports_tcp:
    print(f"Port: {port}")


divider()


cve_list = ["CVE-2019-0708", "CVE-2020-11510", "CVE-2021-19781", "CVE-2022-11580", "CVE-2023-11581"]
print(cve_list)
cve_list.remove("CVE-2022-11580")
print(cve_list)


divider()


attacks = ["Phishing", "Ransomware", "DDoS", "SQL Injection", "XSS", "Zero Day"]
print(attacks)
attacks.reverse()
print(attacks)

i = 0
while i < len(attacks):
    print(f"Attack: {attacks[i]}")
    i += 1

attacks_upper = [attack.upper() for attack in attacks]
print(attacks_upper)


divider()


names = ["John", "Jane", "Jack", "Jill", "James", "Judy"]
ages = [21, 22, 23, 24, 25, 26]

names.remove("Jill")
ages.pop()

for name, age in zip(names, ages):
    print(f"[+] {name} is {age} years old.")


divider()


my_list = [1, 2, 3, 4]
print(my_list)  # [1, 2, 3, 4]
my_list.clear()
print(my_list) # []


divider()


numbers = [1, 2, 4, 5]
other_numbers = [6, 7]

print(numbers)  # [1, 2, 4, 5]
numbers.insert(2, 3)
print(numbers)  # [1, 2, 3, 4, 5]

numbers.extend(other_numbers)
print(numbers)  # [1, 2, 3, 4, 5, 6, 7]