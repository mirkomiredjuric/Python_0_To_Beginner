# print out Hello world
print("Hello world")

#syntax error
#print("She said: "Hello" and than left.")

#print She said: "Hello" and then left.
print('She said: "Hello" and then left')

#print She said: "Hello" and then left.
print("She said: \"Hello\" and then left.")

#print
# Hello world
# Hello world
print("Hello world!\nHello world!")

#print 3 times Hello world one belove another
print("Hello world!\nHello world!\nHello world!")

#print
print("Hello" + " Mire")

#excercise
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#input
input("What is your name?")

#takes input and displays "Hello " + your input
print("Hello " + input("What is your name?"))

#assig
num1 = int(input())
num2 = int(input())
print(num1 * num2)

#display number of letters from input
numOfLetters = len(input())
print(numOfLetters)

#input 2 numbers in variables a and b and than swich them between
a = input()
b = input()

c = a
a = b
b = c
print("a:" + a)
print("b: " + b)

#python variables
name = input("What is your name?") #variable name contains results from input

name = input("What is your name?")
length = len(name)
print(length)

#PROJECT
# Create a greeting for your program. Ask the user for the city that they grew up in. Ask the user for the name of a pet.
# Combine the name of their city and pet and show then their band name. Make sure the input cursor shows on a new line:
print("Welcome to band name generator...")
city = input("Which city did you grow up in?\n")
pet = input("What is the name of a pet?\n")
print("Your band name: " + city + " " + pet +"\n")
