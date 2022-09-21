#!/usr/bin/env python
# coding: utf-8

# In[15]:


#1 Define a function named is_two. It should accept one input and return True if the passed input is either 
#the number or the string 2, False otherwise.

def is_two(n):
    if n ==2 or n == '2':
        return True
    else:
        return False
is_two(1)    

# In[32]:


#2Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(v):
    if v == 'a' or v =='e' or v =='i' or v =='o' or v == 'u':
        return True
    else: 
        return False
    
is_vowel('z')


# In[36]:


#3Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
#Use your is_vowel function to accomplish this.

def is_consonant(c):
    if c == 'a' or c =='e' or c =='i' or c =='o' or c == 'u':
        return False
    else:
        return True
is_consonant('a')


# In[ ]:


def starts_with_vowel(string):
  vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
  for letter in string:
    if letter in vowel and vowel[0]:
      return True
    else:
      return False


# In[63]:


#4Define a function that accepts a string that is a word. The function should capitalize the first letter of the word 
#if the word starts with a consonant. 
#string_name.capitalize()
vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def cap_first_letter(str_word):
    for letter in str_word:
        if letter in vowel and vowel[0]:
            return str_word
        else:
            return str_word.capitalize()
cap_first_letter('tear')


# In[69]:


#5Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill 
#total, and return the amount to tip.
def calculate_tip(tip_percentage, bill_total):
    return tip_percentage * bill_total


# In[71]:


calculate_tip(.2, 50)


# In[73]:


#6Define a function named apply_discount. It should accept a original price, and a discount percentage, and return 
#the price after the discount is applied.

def apply_discount(original_price, discount_percent):
    return original_price - (original_price * discount_percent)


# In[74]:


apply_discount(100, .2)


# In[77]:


#7Define a function named handle_commas. It should accept a string that is a number that contains commas in it as 
#input, and return a number as output.

def handle_commas(number_as_string):
    return number_as_string.replace(',','')


# In[ ]:


#USE str.replace() TO REMOVE A COMMA FROM A STRING IN PYTHON
#Call str.replace(',', '') to replace every instance of a ',' in str with ''.


# In[78]:


handle_commas('1000,000')


# In[81]:


#8Define a function named get_letter_grade. It should accept a number and return the letter grade associated with 
#that number (A-F).
def get_letter_grade(number):
    grade = int(number)
    if grade>=90:
        print('A')
    elif grade>=80:
        print('B')
    elif grade>=70:
        print('C')
    elif grade>=60:
        print('D')
    else:
        print('F')

get_letter_grade(88)


# In[85]:


#9Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(string):
    vowel = "aeiouAEIOU"
    for letter in string:
        if letter in vowel:
            string = string.replace(letter, "")
    return string
remove_vowels('Sequoia')


# In[89]:


#10Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#anything that is not a valid python identifier should be removed
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores
#for example:
#Name will become name
#First Name will become first_name
#% Completed will become completed

def normalize_name(string):
    string = string.strip()
    string = string.lower()
    string = string.replace(' ','_')

    return(string)


# In[90]:


normalize_name('  Tree house  ')


# In[ ]:


def Cumulative(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]


# In[ ]:


def Cumulative(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]


# In[97]:


#11Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum 
#of the numbers in the list.
#cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
#Additional Exercise
#Once you've completed the above exercises, follow the directions from 
# https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 
#in order to thouroughly comment your code to explain your code.

def cumulative_sum(lists):
    cum_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]
 

cumulative_sum([1, 1, 1])


# In[ ]:


#Bonus
#Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
#Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
#col_index('A') returns 1
#col_index('B') returns 2
#col_index('AA') returns 27

