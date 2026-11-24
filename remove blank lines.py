# Write a program to remove blank lines and save the result in another file.
with open("student.txt", "r") as file:
    lines = file.readlines()

with open("new_student.txt", "w") as file:
    for line in lines:
        if line.strip():
            file.write(line)