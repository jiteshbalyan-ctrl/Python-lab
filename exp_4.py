# create a program that prompts the user for a list of numbers and then sorts them in ascending order
number_list =[]
print("If you don't want to enter another number type n")
while True:
    input_user = input("Enter a number : ")
    if input_user.strip().casefold() == 'n':
            break
    input_number = int(input_user)
    number_list.append(input_number)
    
number_list.sort()
print("The numbers in ascending order are:", number_list)
