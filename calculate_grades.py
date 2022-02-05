# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math


def calculate_grades():
    grade_list = get_grade_list()
    # Calculate the mean and standard deviation of the grades
    mean = calculate_mean(grade_list)
    sd = calculate_std(grade_list, mean)
    print_stat(mean, sd)


def print_stat(mean, sd):
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')


def calculate_mean(grade_list):
    total = 0  # total of all grades
    for grade in grade_list:
        total += grade
    return total / len(grade_list)


def calculate_std(grade_list, mean):
    sd = 0  # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    return math.sqrt(sum_of_sqrs / len(grade_list))


def get_grade_list():
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list


calculate_grades()
