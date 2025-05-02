# import arrr
# from pyscript import document


# def translate_english(event):
#     input_text = document.querySelector("#english")
#     english = input_text.value
#     output_div = document.querySelector("#output")
#     output_div.innerText = arrr.translate(english)



"""
1. create a quate collector app using pyfiglet module.
   i. Install Pyfiglet 
   ii. Display quote collector in a fancy way using figlet_format method in pyfiglet
   iii. Collect user input name and quote
   iv. Using a while check if the user input is empty or not, if it is empty then ask the user to enter a valid name and quote
   v. Using try, except and finally block to handle quotes 
"""

# 1. Create a qoute collector app using pyfiglet module
#     i. install a module named pyfiglet
#     ii. display Quote Collector in a fancy way using figlet_format method in pyfiglet
#     iii. collect user input name and quote
#     iv. using a while check if the user input is empty or not, if it is empty then ask
#       the user to enter a valid name and quote
#     v. using try, expect and finally block to handle quotes storing, store the quote
#       in a file name quote.txt and format text this way 
#        "{name} said: {quote}"
#       in the try block and if there is an error then print the error message in the
#       except block and finally block will be used to tell the user thanks for sharing
#       your quote and to close the file


# 2.Mini To-Do List App
#     i. install module named colorama
#     ii. from colorama make use of Fore, and Style
#     iii. collect user input for the task name and mark task as done
#     iv. using a while check if the user input is empty or not, if it is empty then ask
#       the user to enter a valid task name and mark task as done
#     v. print the task name in red color and mark task as done in green color using colorama
#     v. using try, expect and finally block to handle task storing, store the task
#       in a file name task.txt and format text this way 
#        "{task} - {done}"
#       in the try block and if there is an error then print the error message in the
#       except block and finally block will be used to tell the user thanks for sharing
#       your task and to close the file

# 3. Daily Expense Tracker
#     i. install a module named tabulate
#     ii. from tabulate make tabulate
#     iii. collect user input for the expense name, amount and date
#     iv. using a while check if the user input is empty or not, if it is empty then ask
#       the user to enter a valid expense name, amount and date
#     v. using try, expect and finally block check if the amount is a number or not, if it is not a number then ask
#       the user to enter a valid amount
#     v. print the expense name, amount and date in a table format using tabulate with the headers Description, Amount and Date
#     vi. using try, expect and finally block to handle expense storing, store the expense
#       in a file name expense.txt and format text this way 
#        "{expense} - {amount} - {date}"
#       in the try block and if there is an error then print the error message in the
#       except block and finally block will be used to tell the user thanks for sharing
#       your expense and to close the file


import pyfiglet

print(pyfiglet.figlet_format("Quote Collector"))


while True:
    name = input("Enter your name: ").strip()
    quote = input("Enter your quote: ").strip()

    if name and quote:
        break
    else:
        print("Both name and quote are required. Please try again.\n")

try:
    with open("quote.txt", "a") as file:
        file.write(f"{name} said: {quote}\n")
except Exception as e:
    print("An error occurred while saving your quote:", e)
finally:
    print("Thanks for sharing your quote!")
 