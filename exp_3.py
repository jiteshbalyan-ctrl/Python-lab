# # calculate factorial of a number
# num = int(input("Enter a number : "))
# a = 1
# for i in range (1,num+1):
#     a = a * i
#     i +=1
# print("The factorial of the number is : ",a)

# calculate factorial using while loop
num = int(input("Enter a number :"))
f = 1
i = 1
while i<=num:
    f = i * f
    i += 1
    print(f)

    