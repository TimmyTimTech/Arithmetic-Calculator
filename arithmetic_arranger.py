#prompt user for input.
user_input = input("Enter the equation :")

#convert string into array using the split().
array_input = user_input.split()

if ("*" not in user_input) and ("/" not in user_input):
    
    def arithmetic_arranger(array_input,answear=False):

        result = []
            
        #loop through array and conert to integer and indicat indicate to the computer that the indexes has expressions by using the "eval()" function. 

        for int_list in array_input:
            try:
                feeback =  eval(int_list)
                if answear == True:
                    result.append(feeback)
                    continue
                else:
                    answear_false(array_input)
                    break
            except ValueError:
                print ("Error: Numbers must only contain digits.") 

        if len(result) > 0:
            #call the equation function with the appropiate parameters.
            equation_placement(array_input, result)
    

    #condition to check which index of array is being used and triggering the corresponding methond
    def equation_placement(array_input, result):
        if len(array_input) == 1:
            if array_input[0]:
                print(f"{ array_input[0]}----{result[0]}")
            else:
                pass
        elif len(array_input) == 2:
            if array_input[1]:
                print(f"{ array_input[0]}----{result[0]}")
                print(f"{ array_input[1]}----{result[1]}")
            else:
                pass
        elif len(array_input) == 3:
            if array_input[2]:
                print(f"{ array_input[0]}----{result[0]}")
                print(f"{ array_input[1]}----{result[1]}")
                print(f"{ array_input[2]}----{result[2]}")
            else: 
                pass
        elif len(array_input) == 4:
            if array_input[3]:
                print(f"{ array_input[0]}----{result[0]}")
                print(f"{ array_input[1]}----{result[1]}")
                print(f"{ array_input[2]}----{result[2]}")
                print(f"{ array_input[3]}----{result[3]}")
            else:
                pass
        elif len(array_input) == 5:
            if array_input[4]:
                print(f"{ array_input[0]}----{result[0]}")
                print(f"{ array_input[1]}----{result[1]}")
                print(f"{ array_input[2]}----{result[2]}")
                print(f"{ array_input[3]}----{result[3]}")
                print(f"{ array_input[4]}----{result[4]}")
        else:
            print ("Error: Too many problems.")

    def answear_false(array_input) :
        if len(array_input) == 1:
            if array_input[0]:
                print(f"{ array_input[0]}----")
            else:
                pass
        elif len(array_input) == 2:
            if array_input[1]:
                print(f"{ array_input[0]}----")
                print(f"{ array_input[1]}----")
            else:
                pass
        elif len(array_input) == 3:
            if array_input[2]:
                print(f"{ array_input[0]}----")
                print(f"{ array_input[1]}----")
                print(f"{ array_input[2]}----")
            else: 
                pass
        elif len(array_input) == 4:
            if array_input[3]:
                print(f"{ array_input[0]}----")
                print(f"{ array_input[1]}----")
                print(f"{ array_input[2]}----")
                print(f"{ array_input[3]}----")
            else:
                pass
        elif len(array_input) == 5:
            if array_input[4]:
                print(f"{ array_input[0]}----")
                print(f"{ array_input[1]}----")
                print(f"{ array_input[2]}----")
                print(f"{ array_input[3]}----")
                print(f"{ array_input[4]}----")
        else:
            print ("Error: Too many problems.")
    #call the arithmetic_arranger function with parameter of the array
    arithmetic_arranger(array_input,True)

else:
    print("Error: Operator must be '+' or '-'.")
