### 1. Identify the data type of the following values:
# 99.9 float
#"False" str
#False bool
#'0' str
#0 int
#True bool
#'True' str
#[{}] [{}] list
#{'a': []} dict
###


#2.What data type would best represent:
#A term or phrase typed into a search box? string
#If a user is logged in? bool
#A discount amount to apply to a user's shopping cart? float
#Whether or not a coupon code is valid? boolean
#An email address typed into a registration form? string
#The price of a product? float
#A Matrix? list of list
#The email addresses collected from a registration form? list
#Information about applicants to Codeup's data science program? table


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
mer = 3
bro = 5
herc = 1
price_rate = 3
total_rate = (mer + herc + bro) * price_rate
#5. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook,
#they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, 
# and Facebook 350. How much will you receive in payment for this week? You worked 10 
#hours for Facebook, 6 hours for Google and 4 hours for Amazon.
g_rate = 400
am_rate =380
fb_rate = 350

g_hours = 6
am_hours = 4
fb_hours = 10

g_pay = g_rate * g_hours
am_pay = am_rate * am_hours
fb_pay = fb_rate * fb_hours

paycheck = g_pay + am_pay + fb_pay

#6. A student can be enrolled to a class only if the class is not full and the 
#class schedule does not conflict with her current schedule.
class_has_space = True
schedule_has_time = True
enrollment = class_has_space and schedule_has_time

#7. A product offer can be applied only if people buys more than 2 items, and the 
#offer has not expired. Premium members do not need to buy a specific amount of products.
#product_offer = offer not expired and product_amout > 2 or premium-member
offer_active = True
premium_member = False
more_than_two = True
product_offer = (premium_member or more_than_two) and offer_active

#8. Continue working in your data_types_and_variables.py file. Use the following code to follow the instructions below:
#username = 'codeup'
#password = 'notastrongpassword'
#Create a variable that holds a boolean value for each of the following conditions:
#the password must be at least 5 characters
check_one = len(my_password) >= 5 char
#the username must be no more than 20 characters
check_2 = my_username <= 20
#the password must not be the same as the username
check_3 = my_password != my_username
#bonus neither the username or password can start or end with whitespace
check_4 = my_username != ' ' and my_password != ' '
