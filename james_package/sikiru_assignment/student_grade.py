student_numbers = 0
subject_numbers = 0


def number_of_student():
    global student_numbers
    numbers_of_student = int(input("Enter the number of student: "))
    if (numbers_of_student > 0) and (numbers_of_student < 100):
        student_numbers = numbers_of_student
        number_of_subject()
    else:
        print("invalid input: ")
    number_of_student()


def number_of_subject():
    global subject_numbers
    numbers_of_subject = int(input("Enter the numbers of subject: "))
    if (numbers_of_subject > 0) and (numbers_of_subject < 100):
        subject_numbers = numbers_of_subject
    else:
        print("invalid input: ")
    student_input()


def student_input():
    lists = [[None] * student_numbers for _ in range(subject_numbers)]
    for num in range(1, student_numbers + 1):
        for nums in range(1, subject_numbers + 1):
            print(f"Enter the score of student: {num}")
            print(f"Enter the score of subject: {nums}")
            subject_scores = int(input())
            lists[num - 1][nums - 1] = subject_scores


def main():
    number_of_student()


if __name__ == "__main__":
    main()
