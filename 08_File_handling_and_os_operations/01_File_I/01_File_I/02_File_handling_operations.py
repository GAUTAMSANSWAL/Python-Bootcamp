'''
Python provides several modes for opening files:

'r' (Read mode): Opens the file for reading. This is the default mode. If the file doesn't exist, you'll get an error.
'w' (Write mode): Opens the file for writing. If the file exists, its contents will be overwritten. If the file doesn't exist, a new file will be created.
'a' (Append mode): Opens the file for appending. Data will be added to the end of the file. If the file doesn't exist, a new file will be created.
'''
# Opening a file for reading
f = open('gautam.txt', 'r')
content = f.read()
print(content)
f.close()

# Opening a file for writing
string = "This is a new line.\n welcome to python file handling. \n This is the third line."
f = open('gautam.txt', 'w')
f.write(string)
f.close()

# Opening a file for appending
string1 = "This is the fourth line. \n This was appended to the file."
f = open('gautam.txt', 'a')
f.write(string1)
f.close()

# Using 'with' statement to handle files (automatically closes the file)
with open('gautam.txt', 'r') as f:
    content = f.read()
    print(content)
with open('gautam.txt', 'w') as f:
    f.write("This is a new line.\n welcome to python file handling. \n This is the third line.")
with open('gautam.txt', 'a') as f:
    f.write("This is the fourth line. \n This was appended to the file.")

