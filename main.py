import random


def print_timetable(_time_table):
    msg = "[\n"
    for periods in _time_table:
        msg += str(periods) + ",\n"
    msg += "]"
    return msg


number_of_days = int(input("Enter number of days: "))
number_of_periods = int(input("Enter number of periods: "))

save_sub = input("Would you like to read subjects from subjects.txt?: ")
if save_sub.lower().startswith("y"):
    with open("subjects.txt", "r") as f:
        subjects = [data.strip("\n") for data in f]
        subjects_count = len(subjects)
else:
    subjects_count = int(input("Enter number of subjects: "))
    subjects = [str(input(f"{i}. Enter subject name: ")).title() for i in range(1, subjects_count + 1)]

time_table = []
for i in range(number_of_days):
    time_table.append([])
    for _ in range(number_of_periods):
        time_table[i].append(random.choice(subjects))
print(print_timetable(time_table))

save_sub = input("Would you like to save the subjects?: ")
if save_sub.lower().startswith("y"):
    with open("subjects.txt", "w") as f:
        f.write("\n".join(subjects))
