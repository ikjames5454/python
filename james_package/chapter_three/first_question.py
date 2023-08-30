# 3.1
# (Validating User Input) Modify the script of Fig. 3.3 to validate its inputs. For any
# input, if the value entered is other than 1 or 2, keep looping until the user enters a correct
# value. Use one counter to keep track of the number of passes, then calculate the number
# of failures after all the user’s inputs have been received.

passes = 0
failure = 0
score = 0
while score<10:
    individual_score = int(input("individual score"))
    if individual_score == 8:
        print("correct")
        break
    if individual_score == 1:
        passes = passes + 1
    else:
        failure = failure + 1
    score = score + 1
print("number of passes :",passes)
print("number of failure :",failure)





