import argparse

parser = argparse.ArgumentParser(description="Count lines in a file")

parser.add_argument("filename", type = str, help="Name of the file to count lines")
args = parser.parse_args()
with open(args.filename, 'r') as file:
    lines = file.readlines()
    print(f"The file '{args.filename}' has {len(lines)} lines.")