# input_numbers = input("20 30 25 70 55")

# input_numbers = input("Enter a list of integers separated by spaces: ")

# print(input_numbers)

# input_numbers = input("20 30 25 70 55")
# numbers = [int(x) for x in input_numbers.split()]

# sum_of_numbers = sum(numbers)

# print(f"The sum of the number is: {sum_of_numbers}")

# input_numbers = input("Enter a list of integers separated by spaces: ")
# numbers = [int(x) for x in input_numbers.split()]

# sum_of_numbers = sum(numbers)

# print(f"The sum of the numbers is: {sum_of_numbers}")

#creating a tuple

# favorite_books = ( "Atomic Habits", "The Richest Man in babylon", "The Smart Money Woman", "Business Accelerator", "As a Man Thinketh.")
# for book in favorite_books:
#     print(book)

#dictionary program
#get users to fill neccessary information.
# def get_user_input(prompt):
#     while True:
#         user_input = input(prompt)
#         if user_input.strip():
#             return user_input
#         else:
#             print(f"Please enter the valid information.")



# 
# Function to get user input and create new set of intgers
def get_integer_set(prompt):
    while True:
        try:
            user_input = input(prompt)
            integer_set = {int(x) for x in user_input.split()}
            return integer_set
        except ValueError:
            print("Please enter valid integers.")


set1 = get_integer_set("Enter integers for the first set (space-separated): ")

set2 = get_integer_set("Enter integers for the second set (space-separated): ")

# Find the common elements
common_elements = set1.intersection(set2)

# Display the result
print(f"Common elements in both sets: {common_elements}")


