#if and else
print("Welcome to the rollercoster!")
height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you have to grow taller before you can ride")
    
#odd or even number
number = int(input())

if number % 2 == 0:
    print("This is even number.")
else:
    print("This is odd number.")
    
#another example
print("Welcome to the rollercoster!")
height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age >=12 and age <20:
        print("Please pay $10.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride")
    
#BMI 2.0
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >=18.5 and bmi <25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >=25 and bmi <30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >=30 and bmi <35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
  
#leap year
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
  
#true love calculator
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combine_names = name1 + name2
#lowercase name
lower_names = combine_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e
combine_digit = str(first_digit) + str(second_digit)
combine_digit_int = int(combine_digit)
if combine_digit_int < 10 or combine_digit_int > 90:
  print(f"Your score is {combine_digit_int}, you go together like coke and mentos.")
elif combine_digit_int >=40 and combine_digit_int <=50:
  print(f"Your score is {combine_digit_int}, you are alright together.")
else:
  print(f"Your score is {combine_digit_int}.")


#project
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input(print("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n"))
if direction == "left":
  desision =  input(print("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat."
          "Type \"swim\" to swim across.\n"))
  if desision == "wait":
      color = input(print(
          "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"))
      if color == "red":
          print("Burned by fire. Game over")
      elif color == "yellow":
          print("You win")
      elif color == "blue":
          print("Eaten by beasts. Game over")
      else:
          print("Game over")
  else:
   print("Attacked by trout. Game over")
else:
    print("Fall into a hole. Game over.")