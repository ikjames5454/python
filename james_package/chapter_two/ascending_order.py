# (Sort in Ascending Order) Write a script that inputs three different floating-point
# numbers from the user. Display the numbers in increasing order. Recall that an if state-
# ment’s suite can contain more than one statement. Prove that your script works by run-
# ning it on all six possible orderings of the numbers. Does your script work with duplicate
# numbers? [This is challenging. In later chapters you’ll do this more conveniently and with
# many more numbers.]

first_number = int(input("Enter the first_number: "))
second_number = int(input("Enter the second_number: "))
third_number = int(input("Enter the third_number: "))

if(first_number < second_number) and (first_number < third_number):
    if second_number < third_number:
        print("The number  in increasing order: ",first_number,second_number,third_number)
    else:
        print("the number in increasing order: ",first_number,third_number,second_number)
elif(second_number < first_number) and (second_number < third_number):
    if first_number < third_number:
        print("the number in increasing order: ",second_number,first_number,third_number)
    else:
        print("the number in increasing order: ",second_number,third_number,first_number)
elif(third_number < first_number) and (third_number < second_number):
    if first_number < second_number:
        print("the number in increasing order: ",third_number,first_number,second_number)
    else:
        print("the number in increasing order",third_number,second_number,first_number)

