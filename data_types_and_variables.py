### 1. Identify the data type of the following values:
# 99.9 float
#"False" str
#False bool
#'0' str
#0 int
#True bool
#'True' str
#[{}] [{}]
#{'a': []} invalid syntax
###


#2.What data type would best represent:

#A term or phrase typed into a search box? string
#If a user is logged in? string
#A discount amount to apply to a user's shopping cart? float
#Whether or not a coupon code is valid? boolean
#An email address typed into a registration form? string
#The price of a product?float
#A Matrix? int
#The email addresses collected from distutils.fancy_getopt import fancy_getopt
#from http.client import PAYMENT_REQUIRED
#from xml.dom.pulldom import CHARACTERS
#from a registration form? sting
#Information about applicants to Codeup's data science program?string


#3. For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL.
#'1' + 2, error, TypeError: can only concatenate str (not "int") to str
#6 % 4, 1, 2
#type(6 % 4), int, <class 'int'>
#type(type(6 % 4)), int, <class 'type'>
#'3 + 4 is ' + 3 + 4, error, TypeError: can only concatenate str (not "int") to str
#0 < 0, false, False
#'False' == False, true, False
#True == 'True', false, 
#5 >= -5, true, True
#True or "42", error, True
#6 % 5, 1, 1
#5 < 4 and 1 == 1, true, False
#'codeup' == 'codeup' and 'codeup' == 'Codeup', false, False
#4 >= 0 and 1 !== '1', true, SyntaxError: invalid syntax
#6 % 3 == 0, true, True
#5 % 2 != 0, true, True
#[1] + 2, 3, TypeError: can only concatenate list (not "int") to list
#[1] + [2], [1,2], [1, 2]
#[1] * 2, [1,], [1, 1]
#[1] * [2], error, TypeError: can't multiply sequence by non-int of type 'list'
#[] + [] == [], error, True
#{} + {}, error, TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

#4. You have rented some movies for your kids: The little mermaid (for 3 days), 
#Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet 
#if they're going to like it). If price for a movie per day is 3 dollars, how much 
#will you have to pay? daily_rental = 3, daily_rental * 3 * 5 * 1

#5. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook,
#they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, 
# and Facebook 350. How much will you receive in payment for this week? You worked 10 
#hours for Facebook, 6 hours for Google and 4 hours for Amazon.
#hourly_rate * hours_worked weekly_pay
#Google ghourly rate == 400, ghours_worked == 6, ghourly_rate * ghours_worked == gweekly_pay

#Amazon ahourly rate == 380, ahours_worked == 4, ahourly_rate * ahours_worked == aweekly_pay

#Facebook fhourly rate == 350, fhours_worked == 10, fhourly_rate * fhours_worked == fweekly_pay

#gweekly_pay + aweekly_pay + fweekly_pay == gross_pay 

#6. A student can be enrolled to a class only if the class is not full and the 
#class schedule does not conflict with her current schedule.
 #enrollment == class_not_full and schedule_not_conflict

#7. A product offer can be applied only if people buys more than 2 items, and the 
#offer has not expired. Premium members do not need to buy a specific amount of products.
#product_available == off not expired and product_amout > 2 or premium-member

#8. Continue working in your data_types_and_variables.py file. Use the following code to follow the instructions below:
#username = 'codeup'
#password = 'notastrongpassword'
#Create a variable that holds a boolean value for each of the following conditions:
#the password must be at least 5 characters
#password => 5 char
#the username must be no more than 20 characters
#username =< 20
#the password must not be the same as the username
#password != username
#bonus neither the username or password can start or end with whitespace
#username != ' ' and password != ' '
