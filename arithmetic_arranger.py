#prompt user for input.
user_input = input("Enter the equation :")
#convert string into array using the split().
array_input = user_input.split()
def arithmetic_arranger(array_input):
    #convert the array strings into integer values.
    result = []
    for int_list in array_input:
        try:
            result.append(int(int_list))
        except ValueError:
            print("Inavlid number format.")
    print(result)

arithmetic_arranger(array_input)