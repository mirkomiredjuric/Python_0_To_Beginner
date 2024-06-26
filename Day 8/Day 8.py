def greet_with_name(name):
    print(f"Hello {name}")

greet_with_name("Mirko")

def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"I am at{location}")

greet_with_name("Mirko", location="New York")
greet_with_name(location="New York", name="Mirko" )