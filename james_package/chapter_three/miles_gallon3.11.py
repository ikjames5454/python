# (Miles Per Gallon) Drivers are concerned with the mileage obtained by their auto-
# mobiles. One driver has kept track of several tankfuls of gasoline by recording miles driven
# and gallons used for each tankful. Develop a sentinel-controlled-repetition script that
# prompts the user to input the miles driven and gallons used for each tankful. The script
# should calculate and display the miles per gallon obtained for each tankful. After process-
# ing all input information, the script should calculate and display the combined miles per
# gallon obtained for all tankfuls (that is, total miles driven divided by total gallons used).
import infinity as infinity
number = 0
total_miles_driven = 0
total_gallons = 0
miles_driven = 0
gallons = 0
while number < 2:
    miles_driven = int(input("Enter the miles driven: "))
    gallons = int(input("Enter the gallons(-1 to break): "))
    miles_per_gallon = miles_driven / gallons
    if gallons == -1:
        break
    print("miles/gallon: ", f"{miles_per_gallon:.2f}")

    total_miles_driven = total_miles_driven + miles_driven
    total_gallons = total_gallons + gallons
combined_miles_per_gallon = total_miles_driven / total_gallons
print("total_miles_driven: ",total_miles_driven)
print("total gallons: ", total_gallons)
print("combined_miles_per_gallon: ",f"{combined_miles_per_gallon:.2f}")



