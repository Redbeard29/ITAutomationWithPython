import os

current_dir = os.getcwd()
print(current_dir)


file = open("../../../../../Unworthy.txt")

print(file.read())

file.close()

with open("../../../../../Unworthy.txt") as file:
    print(file.read())

#print file with no whitespace between lines
with open("../../../../../Unworthy.txt") as file:
    for line in file:
        print(line.strip().upper())

#store file lines in an array:

file_two = open("../../../../../Unworthy.txt")
lines = file_two.readlines()
file_two.close()

print(lines)

lines.sort()
print(lines)

with open("../../../../../newTextFile.txt", "w") as file:
    file.write("Testing, testing, 1, 2, 3")