import re


def validating_emails(emails):
    if emails.startswith('@'):
        return "invalid email"
    if emails.count('@') != 1:
        return "invalid email"
    if not re.search(r'\.[a-zA-Z]{2,}$', emails):
        return "invalid email"

    return emails


print(validating_emails("Ikennajames@gmail.com"))
print(validating_emails("ikennajamesgmail.com12"))
print(validating_emails("@@ikennajames@gmail.com"))
print(validating_emails("@ikennajamesgmail.com"))
print(validating_emails("ericmike@gmail.com"))

print()


def email_validator(validator):
    validated = []
    for element in validator:
        if element.startswith("@"):
            print("invalid email")
            continue
        if element.count('@') != 1:
            print("invalid email")
            continue
        if not re.search(r'\.[a-zA-Z]{2,}$', element):
            print("invalid email")
            continue
        validated.append(element)
    return validated


emails = ["Ikennajames@gmail.com", "ikennajamesgmail.com12", "@@ikennajames@gmail.com", "@ikennajamesgmail.com",
          "ericmike@gmail.com"]

print(email_validator(emails))
