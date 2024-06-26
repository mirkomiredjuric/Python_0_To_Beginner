#Data types

#String
print("Hello"[0]) #this is subscripting

#Integer
print(123 + 456)

123_456

#Float

3.14159

#Boolean

True
False

#######################################################################3
num_char = len(input("What is your name?"))
print("Your name has " + num_char + " characters.") #this will break because int can't len

num_char = len(input("What is your name?"))
new_num_char = str(num_char) #converting numbers into string
print("Your name has " + new_num_char + " characters.")

a = 123
type(a)

a = str(123)
type(a)

print( 3 + 5)
print( 7 - 2)
print( 3 * 2)
print( 6 / 3) #returns Float
print (2 ** 3)

#PEMDAS
#()
#**
#*
#/
#* /
#+ -
#multi
#subtraction

print(3 * 3 + 3 / 3 - 3) # 9 + (podelice 3/3) pa - 3

#BMI calculator
height = input()
weight = input()

height_float = float(height)
weight_int = int(weight)
bmi = weight_int / height_float ** 2
print(int(bmi))

#round numbers
print(8 / 3)
print(round(8 / 3)) # 2.666666666666
print(round(8 / 3, 2)) # 2.67
print(round(8 // 3)) #returns int, because any / will return floar

#f-String
score = 4
height = 1.8
isWinning = True
print(f"Your score is: {score}, your height is {height}, you are winning is {isWinning}")

# weeks left
age = input()
max_age = 90
remain_age = max_age - int(age)
remain_weeks = int(remain_age * 52)
print(f"You have {remain_weeks} weeks left.")

# project tip calculator
print("Welcome to the tip calculator!")
total_bill = print("What was the total bill? $")
tipPercent = print("How much tip would you like to give? 10, 12 or 15? ")
numOfPeople = print("How many people to split the bill")
totalBillWithTip = total_bill + total_bill * (tipPercent / 100)
totalPayPerson = float(totalBillWithTip / int(numOfPeople), 2)
print(f"Each person should pay: {totalPayPerson}")