# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("I am Gabriella\n")
        file.write("I am 23 years old\n")
        file.write("Honestly,software development is harder than I thought\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File creation process completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File reading process completed.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Anyway im still here\n")
        file.write("98765\n")
        file.write("One more line appended to the existing content\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File appending process completed.")
