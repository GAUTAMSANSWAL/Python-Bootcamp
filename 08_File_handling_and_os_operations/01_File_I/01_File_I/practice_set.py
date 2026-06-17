'''
1. File I/O Basics

a) Create a text file notes.txt using Python and write "Learning Python is fun!" into it.
b) Open notes.txt, read its content, and print it to the console.
'''
# a)
with open('notes.txt', 'w') as file:
    file.write("Learning Python is fun!")
# b)
with open('notes.txt', 'r') as file:
    content = file.read()
    print(content)

'''
2. Read, Write, and Append Files

a) Write a program that writes three lines of text to a file tasks.txt.
b) Open tasks.txt in append mode and add a new line "Task Completed!".
c) Read the file and print all lines as a list using readlines().
'''
# a)
with open('tasks.txt', 'w') as file:
    file.write("Task 1: Complete the project.\n")
    file.write("Task 2: Review the code.\n")
    file.write("Task 3: Submit the report.\n")
# b)
with open('tasks.txt', 'a') as file:
    file.write("Task Completed!\n")
# c)
with open('tasks.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

'''
3. OS and Shutil Modules
a) Use the os module to:
Print the current working directory
List all files and folders in the current directory
Create a new folder my_folder

b) Use the shutil module to:
Copy a file from one folder to another
Move a file to a new folder
Delete a file (careful: irreversible!)
'''
import os
import shutil
# a)
print("Current working directory:", os.getcwd())
print("Files and folders in the current directory:", os.listdir())
os.mkdir('my_folder')
# b)
shutil.copy('gautam.txt', 'my_folder/notes.txt')
shutil.move('gautam.txt', 'my_folder/notes.txt')
os.remove('my_folder/notes.txt')

'''
4. Creating Command Line Utilities
a) Write a small script count_lines.py that takes a filename as input and prints how many lines are in the file.
b) Write a command-line utility search_word.py that takes two arguments:
A filename
A word to search and prints how many times the word appears in the file.
'''
