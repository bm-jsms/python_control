my_ports = []

my_ports.append(22)
my_ports.append(80)
my_ports.append(443)
my_ports.append(8080)
my_ports.append(8080)


print(my_ports)  # [22, 80, 443, 8080]
print(my_ports[0])  # 22
print(my_ports[3])  # 8080


my_ports.extend([3000, 3306])
my_ports += [8081, 8082]


my_ports = sorted(my_ports)


my_ports = list(set(my_ports))  # Remove duplicates


del my_ports[0]   # Delete the element in the position 0


for i, port in enumerate(my_ports):
    print(f"{i}. Port: {port}")


print(f"\n[+] There are {len(my_ports)} ports available.")
print(f"[+] The highest port is {max(my_ports)} and the lowest port is {min(my_ports)}.")
