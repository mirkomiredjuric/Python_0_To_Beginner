def format_name(f_name, l_name): #function which returns value
    return f"{f_name} {l_name}".title()

name = input("Enter your name: ")
last_name = input("Enter your last name: ")
print(format_name(name, last_name))