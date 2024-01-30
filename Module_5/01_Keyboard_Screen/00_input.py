while True:
    try:
        name = input("\n [+] Enter your name: ")
        age = int(input("\n [+] Enter your age: "))
        print(f"\n [!] Hello {name}, now I know that you are {age} years old!")
        break
    except ValueError:
        print("\n [!] Please enter a valid age!")
        continue
