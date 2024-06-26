import random
 #import module
import my_module #import mine custom module

random_integer = random.randint(1, 10) #range of integers including 1 and 10
print(random_integer)

print(my_module.pi)

random_float = random.random() #range between 0.0 and 0.9999
print(random_float)

#random number between 0.0 and 5
randomfloat = random.random() * 5
print(randomfloat)

#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
#Important, the first letter should be capitalised and spelt exactly like in the example e.g. "Heads", not "heads".
#There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".
#e.g. 1 means Heads 0 means Tails
random_site = random.randint(0, 1)
if random_site == 1:
    print("Heads")
else:
    print("Tails")

#Python List
fruits1 = ["apple", "pear", "orange", "banana"]
print(fruits1)

statsOfAmerica = ["Delawere", "Pennsylvania", "New Jersey", "Georgia"]
print(statsOfAmerica)
print(statsOfAmerica[0]) #prints first one
print(statsOfAmerica[-1]) #prints last one
statsOfAmerica[1] = "Zamena" #replace item in the list
print(statsOfAmerica)
statsOfAmerica.append("Washington") #add new item to the list
print(statsOfAmerica)
addonsState = ["Angelaland", "Jack Bauer Land"] #new list
statsOfAmerica.extend(addonsState) #extend statsOfAmerica with addonsState
print(statsOfAmerica)

###
#You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
#Important: You are not allowed to use the choice() function.
#NOTE: In this exercise, you are working collaboratively with another programmer. They already dealt with input() and writing the code needed to get hold of the names in the input area, so you don't need to worry about that.
#The other programmer has written the code to separate the names in the input area into individual names and puts them inside a List called names. For their code to work correctly, you must enter all the names in the input area followed by comma then space. e.g. name, name, name
#You can try printing names to see what it looks like (but remember to remove that code when you submit the assignment).
#Assume that names works like this:

#input area: x, y, z,
#names = ["x", "y", "z"]
#Example Input
#Angela, Ben, Jenny, Michael, Chloe
#Note: notice that there is a space between the comma and the next name.

#Example Output
#Michael is going to buy the meal today!

names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']
namesLen = len(names)
randomPosition = random.randint(0, namesLen - 1)
print(f"{names[randomPosition]} is going to buy the meal today!")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears" ]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables] #list that contains 2 lists
print(dirty_dozen) #will display list that contains 2 lists [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]
print(dirty_dozen[1][1]) #will display second item from second list

#This is a difficult challenge. 💪
#You are going to write a program that will mark a spot on a map with an X.
#In the starting code, you will find a variable called map.
#This map contains a nested list. When map is printed this is what it looks like, notice the nesting:
#[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
#This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{line1}\n{line2}\n{line3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.
#['⬜️', '⬜️', '⬜️']
#['⬜️', '⬜️', '⬜️']
#['⬜️', '⬜️', '⬜️']
#Now it looks a bit more like the coordinates of a real map:

#Your job is to write a program that allows you to mark a square on the map using a letter-number system.
#So an input of A3 should place an X at the position shown below:
#First, your program must take the user input and convert it to a usable format.
#Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

#[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
#Example Input 1
#B3
#Example Output 1
#Hiding your treasure! X marks the spot.
#['⬜️', '️⬜️', '️⬜️']
#['⬜️', '⬜️', '️⬜️']
#['⬜️️', 'X', '⬜️️']
#Example Input 2
#B1
#Example Output 2
#Hiding your treasure! X marks the spot.
#['⬜️', 'X', '️⬜️']
#['⬜️', '⬜️', '️⬜️']
#['⬜️️', '⬜️️', '⬜️️']
#Hints
#See if this List method helps you: https://www.w3schools.com/python/ref_list_index.asp
#Remember that nested Lists in Python are accessed from outside to inside. e.g. In the List below:
#list = [['A', 'B, 'C'], 'E', 'F', 'G']
#E is list[1] C is list[0][2]
#Check your formatting. This is correctly formatted:
#['⬜️', '⬜️', '⬜️']
#['⬜️', '⬜️', '⬜️']
#['⬜️', 'X', '⬜️']
#vs.
#Incorrectly formatted (missing a space before 'X and extra space after the X and extra space before the comma):
#['⬜️', '⬜️', '⬜️']
#['⬜️', '⬜️', '⬜️']
#['⬜️','X ' , '⬜️']

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

#if
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

#Project: Rock Papaer Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
