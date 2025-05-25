# 1. Write a program to open three files 1.txt, 2.txt and 3.txt 
# if any these files are not present, a message without exiting 
# the program must be printed prompting the same.

# -- using with to open multiple file at a time
filenames = ['file1.txt', 'file2.txt', 'file3.txt']

for filename in filenames:
    try:
        with open(filename, 'r') as file:
            print(f"{filename} opened successfully.")
    except FileNotFoundError:
        print(f"{filename} is not present.")

