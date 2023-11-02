question = input("Enter the question: ")
try:
    integer_number = int(question)
except ValueError:
    print("The cannot be converted to an integer.")

print(integer_number)