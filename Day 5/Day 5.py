fruits = ["Apple", "Peach", "Pear"]
#iterate over loop
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")


#You are going to write a program that calculates the average student height from a List of heights.
#e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#The average height can be calculated by adding all the heights together and dividing by the total number of heights.
#e.g.
#180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
#There are a total of 7 heights in student_heights
#1146 ÷ 7 = 163.71428571428572
#Average height rounded to the nearest whole number = 164

student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
sum = 0
numberOfStudents = len(student_heights)
for i in student_heights:
  sum = sum + i
prosecnaVisina = round(sum / numberOfStudents)
print(f"total height = {sum}")
print(f"number of students = {numberOfStudents}")
print(f"average height = {prosecnaVisina}")

#You are going to write a program that calculates the highest score from a List of scores.
#e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
#Important you are not allowed to use the max or min functions. The output words must match the example. i.e
#The highest score in the class is: x

student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
hightScore = student_scores[0]
for i in student_scores:
  if hightScore < i:
    hightScore = i
print(f"The highest score in the class is: {hightScore}")


#You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:
#i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
#Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
#Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️
sum = 0
for n in range (0, target + 1):
  if n % 2 == 0 :
    sum = sum + n
print(sum)

for number in range(0, 11): #range for numbers from 0 to 10
    print(number)

for num in range(1, 11, 3):
    print(num) #display number from 1 to 10 with increment 3 -> 1, 4, 7, 10

#You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
#Your program should print each number from 1 to 100 in turn and include number 100.
#When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
#e.g. it might start off like this:

#1
#2
#Fizz
#4
#Buzz
#Fizz
#7
#8
#Fizz
#Buzz
#11
#Fizz
#13
#14
#FizzBuzz

for num in range (1, 101):
    if num % 3 == 0  and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#project PyPassword Generator
print()