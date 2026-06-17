import argparse

parser = argparse.ArgumentParser(description='count occurence of a word in a file')

parser.add_argument('filename', type=str, help='the name of the file to search')
parser.add_argument('word', type=str, help='the word to search for')

args = parser.parse_args()

with open(args.filename, 'r') as file:
    count = 0
    content = file.read()
    words = content.split(" ")
    for w in words:
        if w == args.word:
            count += 1
print(f"The word '{args.word}' occurs {count} times in the file.")