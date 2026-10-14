# prompt user for their age and tells them if they can vote in the next election
age = int(input("Enter you age : "))
if age<=18:
    print("You cannot vote you minor !!!")
else :
    print("You can vote :)")