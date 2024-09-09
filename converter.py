# function that converts decimal numbers to binary numbers
def convert_to_binary(decimal_number):
    
    # turns the string into integers 
    decimal_number = int(decimal_number)
    
    # when the decimal is divisible by 2, a 0 is placed in the string and when it's not, it places 1 in the string just like a binary number
    num_list = ''
    if decimal_number % 2 == 0:
        num_list += '0'
    else:
        num_list += '1'
    
    # quotient is a variable that gets the remainder of the decimal when its divided by 2 as a whole number
    quotient = decimal_number // 2
    
    # while loop that keeps going until quotient becomes 0. When the decimal is divisible by 2, a 0 is placed in the string and when it's not, it places 1 in the string just like a binary number
    while quotient != 0:
        if quotient % 2 == 0:
            num_list = '0' + num_list
        elif quotient % 2 != 0:
            num_list = '1' + num_list
        quotient = quotient // 2
    return num_list

# function that converts binary numbers to decimal numbers
def convert_to_decimal(binary_number):

    # reversing the binary numbers
    reverse = ''
    for i in binary_number:
        reverse = i + reverse
    
    # defining the result as a temporary 0 which will be added onto later for the final decimal number
    result = 0
    
    # in the order of the index, the 1 will be multiplied to the index by power of 2's
    index = 0
    for i in reverse:
        if reverse[index] == '1':
            result += (2**index)
        index += 1

    # printing the result
    print('Decimal number:', result)  

# function that displays the menu options and asks for user input
def get_menu_choice():
    print("\n*** Menu ***")
    print("\n1. Convert to binary")
    print("2. Convert to decimal")
    print("3. Binary counting")
    print("4. Quit")
    user_input = input("\nWhat would you like to do [1,2,3,4]? ")
    
    # if the user input is invalid, this will appear and ask for an input again
    while user_input != '1' and user_input != '2' and user_input != '3' and user_input != '4':
        print("Invalid choice, please enter either 1, 2, 3 or 4.")
        user_input = input("\nWhat would you like to do [1,2,3,4]? ")
    
    return user_input

# calls get_menu_choice function and is under the variable named user_input
user_input = get_menu_choice()

# while loop that accepts user input 1,2, and 3
while user_input == '3' or user_input == '2' or user_input == '1':
    
    if user_input == '1':
        # asks for a number from user
        decimal_number = input('\nPlease enter number: ')
        
        # if the user inputs letters instead of digits, this error message will appear and asks for an input with digits only
        while decimal_number.isdigit() == False:
            print('Please make sure your number contains digits 0-9 only.')
            decimal_number = input('\nPlease enter number: ')
        
        # print statement that calls for convert_to_binary function and prints out the result
        print('\nBinary number:', convert_to_binary(decimal_number))
        
    elif user_input == '2':
        binary_number = input('\nPlease enter binary number: ')
        
        # while loop that makes sure that the user is only submitting 1's and 0's to the input instead of letters or other digits and if there is, it will ask for another input with only 1's and 0's
        index = 0
        while index < len(binary_number):
            while binary_number[index] != '0' and binary_number[index] != '1':
                print('Please make sure your number contains digits 0-1 only.')
                binary_number = input('\nPlease enter binary number: ')
            index += 1
        print('')
        
        # calls for convert_to_decimal function
        convert_to_decimal(binary_number)
        
    elif user_input == '3':
        decimal_number = input('\nPlease enter number: ')
        
        
        # if the user inputs letters instead of digits, this error message will appear and asks for an input with digits only
        while decimal_number.isdigit() == False:
            print('Please make sure your number contains digits 0-9 only.')
            decimal_number = input('\nPlease enter number: ')
            
        print('')
        
        # turns the decimal_number string into integers
        decimal_number = int(decimal_number)
        
        # for and while nested loop that displays conversion for every number from 1 until the number the user inputs
        count = 1
        for i in range(1, decimal_number + 1):    
            while count <= i:
                print('Decimal:', count, '= binary:', convert_to_binary(i))
                count += 1
    
    # prompts for another user_input while the user doesn't want to quit yet
    print('')
    user_input = get_menu_choice()

# when user input is 4, this appears
print('\nGoodbye.')