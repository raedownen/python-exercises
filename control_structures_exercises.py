#1.Conditional Basics

#a. prompt the user for a day of the week, print out whether the day is Monday or not
day_of_week = input("What day is today?:\n")
if day_of_week == "Monday":
    print("Yes, it is Monday!")
else:
    print("It is definitely not Monday!")
    
# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day_of_week = input("What day is today?:\n")
if day_of_week == ('Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday'):
    print("Yes, it is weekday!")
else:
    print("It is definitely the weekend!")

#c. create variables and make up values forgit 
#the number of hours worked in one week
#the hourly rate
#how much the week's paycheck will be
#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
weekly_hours = 40
hourly_rate = 100
overtime_hours = 20
overtime_rate = 150
weekly_paycheck = (weekly_hours * hourly_rate) + (overtime_hours * overtime_rate)

#2. Loop Basics
#a. While
#Create an integer variable i with a value of 5. Create a while loop that runs so long as i is less than or equal to 15. 
# Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2
#Alter your loop to count backwards by 5's from 100 to -10.
countdown = 100

while countdown > -11:
    print ('CountDown = ', countdown)
    countdown = countdown - 5

#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
sample_list = [2,4,16,256]
result = [number ** 2 for number in sample_list]
print(result)
 
#Write a loop that uses print to create the output shown below.
countdown = 100
while countdown > 4:
    print (countdown)
    countdown = countdown - 5

#b. For Loops

    i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
num = int(input("Display multiplication table of? "))

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


    ii. Create a for loop that uses print to create the output shown below.


#c. break and continue

    #i. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
n = int(input("Enter a positive integer: "))
while n > 1:
    n -= 1
    print(n)
print('Loop ended.')

#ii. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number 
# and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)
num = eval(input('Enter a number: '))
i = 1
while i > 0 :
  print(i)
  if i == num:
    break
  i += 1

#iii. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered.


#3. Fizzbuzz
#One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, 
# the test is designed to test basic looping and conditional logic skills.
#Write a program that prints the numbers from 1 to 100.
#For multiples of three print "Fizz" instead of the number
#For the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1, 101):
    if i%3 == 0 and i%5 ==0:
        print("FizzBuzz")
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print("Buzz")
    print(i)


#4. Display a table of powers.
#Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.


5. Convert given number grades into letter grades.

    Prompt the user for a numerical grade from 0 to 100.
    Display the corresponding letter grade.
    Prompt the user to continue.
    Assume that the user will enter valid integers for the grades.
    The application should only continue if the user agrees to.
    Grade Ranges:

    A : 100 - 88
    B : 87 - 80
    C : 79 - 67
    D : 66 - 60
    F : 59 - 0


6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

a. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.