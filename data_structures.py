#Question 1; calculating sum of integers
user_input = input(1,5,8,9,19)
integer_list = [int(x) for x in user_input.split()]

sum_of_integers = sum(integer_list)
print("Sum of the integers:", sum_of_integers)

#Question 2;Print book names using a tuple
  # Create a tuple of book names
favorite_books = ("The Hitchhiker's Guide to the Galaxy",
                  "The Lord of the Rings",
                  "Pride and Prejudice",
                  "To Kill a Mockingbird",
                  "The Martian")
# Print each book name on a new line (using a for loop)
for book in favorite_books:
    print(book)

#Question 3; Create and print a dictionary
    # Create an empty dictionary
person_info = {}
# Get user input for name, age, and favorite color
person_info["name"] = input("Gabriella")
person_info["age"] = int(input("22"))
person_info["favorite_color"] = input("Pink")

# Print the dictionary contents
print("Person Information:")
print(person_info)


#Question 4; common elements between two sets

set1_input = input(1,2,4,6,9)
set2_input = input(3,4,6,9,24 )

set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))

common_elements = set1.intersection(set2)
print("Common elements in both sets:", common_elements)


#Question 5; creating new list of words with odd numbers
    # Create a list of words
words = ["apple", "banana", "orange", "grapefruit", "mango"]

# Use list comprehension to filter words with odd length
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the list of words with odd length
print("Words with odd number of characters:", odd_length_words)
