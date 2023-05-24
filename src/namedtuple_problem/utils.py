from collections import namedtuple

def calculate_average_mark(students_data):
    N = int(students_data[0])
    Students = namedtuple('students', students_data[1])
    total = 0

    for i in range(N):
        student = Students(*students_data[i+2].split())
        total += int(student.mark)

    average_mark = total / N
    print(format(average_mark,'.2f'))
    return(format(average_mark,'.2f'))

