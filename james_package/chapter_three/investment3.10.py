# 2.12 (7% Investment Return) Some investment advisors say that it’s reasonable to ex-
# pect a 7% return over the long term in the stock market. Assuming that you begin with
# $1000 and leave your money invested, calculate and display how much money you’ll have
# after 10, 20 and 30 years. Use the following formula for determining these amounts:
# a = p(1 + r)n
# where
# p is the original amount invested (i.e., the principal of $1000),
# r is the annual rate of return (7%),
# n is the number of years (10, 20 or 30) and
# a is the amount on deposit at the end of the nth year.

# 3.10(7% Investment Return) Reimplement Exercise 2.12 to use a loop that calculates
# and displays the amount of money you’ll have each year at the ends of years 1 through 30.
p = 1000
r = 7 / 100
print("Number of years\t\t", "Amount in each year")
print()
for n in range(1,31):
    a = p * (1 + r) ** n
    print(f"year {n}\t\t\t\t\t ", f"{a:.2f}")
