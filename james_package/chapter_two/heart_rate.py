# (Target Heart-Rate Calculator) While exercising, you can use a heart-rate monitor
# to see that your heart rate stays within a safe range suggested by your doctors and trainers.
# According to the American Heart Association (AHA) (http://bit.ly/AHATargetHeart-
# Rates), the formula for calculating your maximum heart rate in beats per minute is 220
# minus your age in years. Your target heart rate is 50–85% of your maximum heart rate.
# Write a script that prompts for and inputs the user’s age and calculates and displays the
# user’s maximum heart rate and the range of the user’s target heart rate. [These formulas
# are estimates provided by the AHA; maximum and target heart rates may vary based on
# the health, fitness and gender of the individual. Always consult a physician or qualified
# healthcare professional before beginning or modifying an exercise program.]
# 2.14

user_age = int(input("Enter your Age : "))
maximum_heart_rate = 220 - user_age
range_minimum = 50/100 * maximum_heart_rate
range_maximum = 85/100 * maximum_heart_rate
print("The maximum_heart_rate: ",maximum_heart_rate,"\nThe range_minimum: ",f"{range_minimum:.2f}","\nThe range_maximum: ",f"{range_maximum:.2f}")