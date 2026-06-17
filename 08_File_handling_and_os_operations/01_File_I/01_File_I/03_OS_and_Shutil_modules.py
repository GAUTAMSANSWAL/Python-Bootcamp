# Python's os module provides functions for interacting with the operating system, such as working with directories and files.
import os

# listing all files and directories in the current directory
a = os.listdir(".")
print(a)

# Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# Checking if a file or dir exists
file_exists = os.path.isfile('gautam.txt')
print(os.path.exists("any directory"))

# to delete a file or directory
os.remove('any file')
os.rmdir('any directory') #empty directory only


# Python's shutil module provides functions for high-level file operations, such as copying and moving files.
import shutil

# delete a directory and all its contents
shutil.rmtree('any directory')

# Copy a file
shutil.copy('source_file.txt', 'destination_file.txt')

# Move a file
shutil.move('source_file.txt', 'destination_directory/')