students = ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female',
            'male', 'female', 'male', 'female', 'male', 'male', 'male', "Female"]


def count_gender(list_of_student):
    number_of_counts = {'male': 0, 'female': 0}
    for sex in list_of_student:
        if sex.casefold() == 'male':
            number_of_counts['male'] += 1
        if sex.casefold() == 'female':
            number_of_counts['female'] += 1

    return list(number_of_counts.items())


print(count_gender(students))


def count_number(student_list):
    number_of_male = 0
    number_of_female = 0
    for gender in student_list:
        if gender.casefold() == "male":
            number_of_male += 1
        if gender.casefold() == "female":
            number_of_female += 1
    return ('male', number_of_male), ('Female', number_of_female)


result = count_number(students)
num = [result]
print(num)

names = ['Joe', 'Hary', 'Kelvin', 'Seyi', 'Ashley', 'Akpan', 'Segun', 'Seyi', 'Muhammed', 'Hakimi', 'Segun', 'Grace',
         'Seyi', 'seyi', 'Samuel', 'segun', 'Sikiru']


def sort(name_list):
    name = {'Seyi': 0, 'Segun': 0, 'Samuel': 0}
    for r in name_list:
        if r == 'Seyi':
            name['Seyi'] += 1
        if r == 'Segun':
            name['Segun'] += 1
        if r == 'Samuel':
            name['Samuel'] += 1

    return dict(name.items())


print(sort(names))


def count(name_of):
    name = {}
    for r in name_of:
        if r.capitalize().startswith("S"):
            # if r.startswith('S') or r.startswith("s"):
            # name_capital = r.capitalize()
            # if name_capital in name:
            #     name[name_capital] += 1
            # else:
            #     name[name_capital] = 1

            name[r.capitalize()] = name.get(r.capitalize(), 0) + 1

    return name


print(count(names))


