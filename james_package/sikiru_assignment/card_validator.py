masterCardType = 0
visaCardType = 0
americaExpressCardType = 0
discoverCardType = 0
verveCardType = 0
list_number = 0
number_holder = str(0)
double_of_evenDigit = 0
sum_of_odd_number = 0
validity = str(0)
length = 0


def collect_number():
    global number_holder
    global list_number
    global length
    card_number = int(input("Hello kindly enter card details to verify: "))
    converter = ""
    number_holder = str(card_number) + converter
    length = len(str(number_holder))
    list_number = [0] * length
    for num in range(length):
        list_number[num] = int(number_holder[num])


def conditions():
    global visaCardType
    global masterCardType
    global americaExpressCardType
    global discoverCardType
    global verveCardType
    if list_number[0] == 4:
        visaCardType = "VisaCard"
    if list_number[0] == 5:
        masterCardType = "MasterCard"
    if list_number[0] == 3 and list_number[1] == 7:
        americaExpressCardType = "America Express Card"
    if list_number[0] == 6:
        discoverCardType = "Discover Card"
    if list_number[0] == 5 and list_number[1] == 0:
        verveCardType = "Verve Card"


def iterate():
    global double_of_evenDigit
    global sum_of_odd_number
    for row in range(len(number_holder) - 1, -1, -1):
        if row % 2 == 0:
            container = list_number[row] * 2
            if container < 10:
                double_of_evenDigit += container
            else:
                containers = str(container)
                for i in range(len(containers)):
                    store = int(containers[i])
                    double_of_evenDigit += store


    for row in range(len(number_holder)):
        if row % 2 != 0:
            sum_of_odd_number += list_number[row]




def sum_and_validity():
    global validity
    sums = double_of_evenDigit + sum_of_odd_number
    if sums % 10 == 0:
        validity = "valid"
    else:
        validity = "invalid"


def condition_met():
    global verveCardType
    global masterCardType
    global americaExpressCardType
    global discoverCardType
    global verveCardType
    global length
    global validity
    if list_number[0] == 4:
        print("***creditcard type: " + str(verveCardType))
    if list_number[0] == 5:
        print("***creditcard type: " + str(masterCardType))
    if list_number[0] == 3 and list_number[1] == 7:
        print("***creditcard type: " + str(americaExpressCardType))
    if list_number[0] == 6:
        print("***creditcard type: " + str(discoverCardType))
    if list_number[0] == 5 and list_number[1] == 7:
        print("***creditcard type: " + str(americaExpressCardType))
    print("***credit card number: " + number_holder)
    print("credit card length: " + str(length))
    print("**creditcard type: " + validity)


def main():
    collect_number()
    conditions()
    iterate()
    sum_and_validity()
    iterate()
    condition_met()


if __name__ == "__main__":
    main()
