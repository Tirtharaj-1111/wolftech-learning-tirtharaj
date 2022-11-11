<<<<<<< HEAD
import json

# Creating text files and reading/writing to and from it
# f1 = open("file-0.txt", "a")

# str1 = "My name is Tirtharaj Mukherjee. Welcome to my first project"
# f1.write(str1)
# f1.close()

# f2 = open("file-0.txt", "r")
# print(f2.read())
# f2.close()

# f1 = open("file-0.txt", "a")
# f1.write("This is a new line")
# f1.close()

# f2 = open('file-0.txt', "r")
# k = f2.read()
# print(k)

# Creating a dictionary and writing to a file
dict1 ={
    "emp1": {
        "name": "Eminem",
        "designation": "Developer",
        "age": "25",
        "salary": "56000"
    },
    "emp2": {
        "name": "Shadows",
        "designation": "Lead Data Scientist",
        "age": "37",
        "salary": "89000"
    },
}

f4 = open("file-1.json", "w")
json.dump(dict1, f4)
=======
import json

# f1 = open("file-0.txt", "a")
#
# str1 = "My name is Tirtharaj Mukherjee. Welcome to my first project"
# f1.write(str1)
# f1.close()

# f2 = open("file-0.txt", "r")
# print(f2.read())
# f2.close()

# f1 = open("file-0.txt", "a")
# f1.write("This is a new line")
# f1.close()

# f2 = open('file-0.txt', "r")
# k = f2.read()
# print(k)

dict1 ={
    "emp1": {
        "name": "Eminem",
        "designation": "Developer",
        "age": "25",
        "salary": "56000"
    },
    "emp2": {
        "name": "Shadows",
        "designation": "Lead Data Scientist",
        "age": "37",
        "salary": "89000"
    },
}

f4 = open("file-1.json", "w")
json.dump(dict1, f4)
>>>>>>> origin/main
f4.close()