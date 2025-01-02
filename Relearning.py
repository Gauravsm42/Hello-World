# print("Hello World")

# ######## Variables ########
# chr_name = "Josh"
# chr_age = "20"
# print("My name is " +chr_name+ ".")
# # print("I'm " +chr_age+ " years old.")
# chr_name = "Tom"
# chr_age = 80  # only chr can be concatenated, not integers. Use str() to convert
# print("And my name \nis " +chr_name+ ".")     # \n adds a new line in the string
# print("I'm \"" +str(chr_age)+ "\" years old.")     # \ followed by " prints " out literally

####### Functions #########
# To access functions, add a period. They can be tacked on in the same line
# phrase = "The Sun is Yellow"
# print(phrase.upper().isupper())
# print(len(phrase))
# print(phrase[0])   # Python starts indexing from 0
# print(phrase.index(" "))   # Space counts as a character
# print(phrase.index("The"))   # Index function is case-sensitive
# print(phrase.replace("Sun", "Moon"))

####### Numbers ########
# from math import *   # This imports additional math functions
# print(4 * (10.6-6.71))
# print(5 % 2)   # % represents mod operation
# num = -5    # Variables can store numbers
# print(str(num) + " is my age")
# print(abs(num))   # Provides absolute value
# print(pow(2, 0))    # Pow raises numbers to specific powers. Here, 2 raised to power of 0
# print(max(1,5,7,6))   # Same can be done with min
# print(round(3.69))   # Rounds to nearest whole number
# print(floor(3.69))   # Chops off anything after decimal, i.e. always rounds the number DOWN
# print(ceil(3.69))   # Always rounds the number UP
# print(sqrt(36))

####### Inputs #######
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# # result = int(num1) + int(num2)   # int can only work with whole numbers
# result = float(num1) + float(num2)
# print(result)

####### Lists ######
# fruits = ["Mango", "Banana", "Kiwi", 2, 5.4, False, "Pear", "Strawberry", "Orange", "Grape"]
# print(fruits[1:6])   # Using : specifies a range, however the last element isn't included
# print(fruits[-1])   # Negative sign can be used to start indexing from last. From last, indexing starts from -1 not 0
# fruits[2] = "Guava"
# print(fruits[2])

###### List Functions #####
# piston_number = [6, 8, 2, 7, 5, 12, 14]
# engine = ["V6", "B7", "F8", "J5", "K14", "L12", "Z2"]
# engine.extend(piston_number)   # Adds other lists to end of original list
# engine.append("A6")   # Adds individual elements to the end of the list
# engine.insert(1, "A6")   # Adds individual elements at specified index positions
# engine.remove("B7")   # Removes exactly element, can't use index no.
# engine.clear()   # Clears the entire list
# engine.pop()   # Removes the last element
# engine.sort()   # Sorts in ascending order
# engine.reverse()   # Reverses the list
# print(engine)
# print(engine.index("J5"))   # Gives index no.
# print(engine.count("J5"))   # Gives no. of occurrences in the list
# engine2 = engine.copy()   # Copies the entire list
# print(engine2)

######## Tuples ########
# num = (4, 8, 1, 6, 7)   # Tuples are immutable, i.e. they can't be modified
# print(num)

###### Functions ######
# def cube_nums(num):
#     print("The cube of " +num+ " is " + str(int(num) ** 3))
#
# cube_nums("3")

# def math(num):
#     num2 = num + num
#     num3 = num2 ** 2
#     return num3   # Return will store the result but will have to be printed separately later
#
# print(math(2))

###### If Statements #####
# ageA = 25
# ageB = 20
#
# if ageA > ageB:
#     print("A is older than B")
# elif ageA < ageB:
#     print("A is younger than B")
# else:
#     print("A is the same age as B")

# is_male = True
# is_tall = False
#
# if is_male and is_tall:
#     print("You're a tall male")
# elif is_male and not(is_tall):
#     print("You're a short male")
# elif not(is_male) and is_tall:
#     print("You're tall, but not male")
# else:
#     print("You're neither male, nor tall")

# def highest_rank(rank1, rank2, rank3):
#     if rank1 <= rank2 and rank1 <= rank3:
#         return rank1
#     elif rank2 <= rank1 and rank2 <= rank3:
#         return rank2
#     else:
#         return rank3
#
# print(highest_rank(4, 8, 9))

####### Basic Calculator ########
# num1 = float(input("Enter first number: "))   # Float converts input to integer
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == "+" or op == "plus" or op == "add":
#     print(num1 + num2)
# elif op == "-" or op == "minus" or op == "subtract":
#     print(num1 - num2)
# elif op == "*" or op == "multiply":
#     print(num1 * num2)
# elif op == "/" or op == "divide":
#     print(num1 / num2)
# else:
#     print("Invalid operator!")

######## Dictionaries ########
# MonthConversions = {
#     "Jan": "January",
#     "Feb": "February",   # These are key-value pairs
#     "Mar": "March",      # "Mar" is the key, "March" is the value
#     "Apr": "April",      # Each key has to be unique
#     "May": "May",        # Keys don't need to be strings, they can be int
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December"
# }
#
# print(MonthConversions["Jan"])
# print(MonthConversions.get("Feb"))   # .get allows to pass in a default in case the key doesn't match in the dictionary
# print(MonthConversions.get("Abc", "Invalid key"))   # It'll print Invalid key as the default

######## While Loops ########
# i = 1
# while i <= 10:
#     print(i)
#     i += 1   # Shorthand for i = i + 1
#
# print("End of Loop")

######### Guessing Game #########
# secret_word = "Monkey"
# guess = input("Enter guess: ")
# guess_count = 0
# guess_limit = 2
# out_of_guesses = False
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         print("Incorrect guess, try again!")
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("You're out of guesses!")
# else:
#     print("Yay! " +secret_word+ " was the correct guess!")

######## For Loops #########
# fruits = ["mango", "kiwi", "apple"]
# for fruit in fruits:
#     print(fruit)
# print(len(fruits))
# for index in range(len(fruits)):
#     print(index)
# for index in range(len(fruits)):
#     print(fruits[index])

# for number in range(10):   # Starts from 0, last element excluded
    # print(number)
# for num in range(3, 10):   # Starts from 0, last element excluded
#     print(num)

# for letter in "Hello There!":
    # print(letter)

# for num in range(5):
#     if num == 0:
#         print("First num!")
#     else:
#         print("Not first")

######### Creating a Exponent Function ############

# def raise_to_pow(base_num, pow_num):
#     return base_num ** pow_num

### OR ###

# def raise_to_pow(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):   # This just gives the number of times the loop will run
#         result = result * base_num
#     return result
#
# print(raise_to_pow(4, 2))

######## 2D Lists & Nested Loops ########
# num_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
#
# # print(num_grid [1] [2])   # These also start with 0
#
# for row in num_grid:   # Loop through every row in the grid
#     for col in row:   # Loop through every column in each row
#         print(col)

######### Building a Translator ###########
# Rules of the language: Every vowel becomes 's'
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":   # If the lower case version of the letter is either a, e, i, o, or u
#             if letter.isupper():   # This takes care if the vowel is capital
#                 translation = translation + "S"
#             else:
#                 translation = translation + "s"
#         else:
#             translation = translation + letter
#     return translation
#
# # print(translate(input("Enter phrase: ")))
# print(translate("It can translate any phrase!"))

####### Another way of writing multiple line comments ########
'''
Anything between three
single quote marks
is not rendered
This can create
multiple line comments
But this isn't
considered Python best practice
'''

######### Try/except Blocks ########
# These help in catching errors
# If there's an error in your code & python can't run it, you can specify what to output

# try:   # Try out this bit of code
#     number = int(input("Enter a number: "))
#     print(number)
# except:   # If try doesn't run, run the except code
#     print("Invalid input")
# But this exception is too broad, you won't be able to tell what the exact error was
# try:
#     value = 10/0
#     print(value)
# except:
#     print("invalid input")
# Here, the error is division by zero, but the exception output is the same

######## Catching multiple errors ##########
# try:
#     value = 10/0
#     print(value)
# except ZeroDivisionError:
#     print("Divided by zero")
# This catches the particular type of error

###### Error Best Practices in Python #######
# try:
#     value = 10/0
#     number = int(input("Enter a number: "))
# except ZeroDivisionError as err:   # This stores the error message as a variable
#     print("err")   # This prints the stored error msg; this way you can find out the type of error that occurred
# except ValueError:
#     print("Invalid input")

######## Reading #########
# fruits = open("fruits.txt", "r")   # r stands for read mode
# w - write, r+ - read & write, a - append
# print(fruits.read())
# print(fruits.readable())   # Tells whether the file is readable
# print(fruits.readlines())   # Reads the entire file and puts it in a list
# print(fruits.readlines()[1])
# for fruit in fruits.readlines():
    # print(fruit)
# fruits.close()   # Always close the file at the end

####### Writing #######
# fruits = open("fruits.txt", "a")
# # fruits.write("Banana - Oct")   # Be careful while writing to a file, the file can be easily messed up
# fruits.write("\nJackfruit - May")   # Adds text to a new line
# fruits.close()

# fruits = open("fruits.txt", "w")
# fruits.write("Apple - Jan")   # Write mode overrides the entire file, erasing previous content
# fruits.close()

# fruits = open("fruits1.txt", "w")
# fruits.write("Apple - Jan")   # Write mode can also be used to create new files
# fruits.close()

# html_fruits = open("fruits.html", "w")
# html_fruits.write("<p>This is fruits HTML</p>")
# html_fruits.close()

######## Modules ######
# Used to import code from external python files
# import useful_tools
# print(useful_tools.get_file_ext("fruits.txt"))
# print(useful_tools.roll_dice(8))
# Look up python modules list for an exhaustive list of default modules
# 3rd party modules can also be installed

######## pip ########
# Package manager used to manage modules
# Use command prompt to run pip
# Run 'pip --version' to check if pip is installed