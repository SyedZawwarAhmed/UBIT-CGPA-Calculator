import csv


def calculate_cgpa(marks):
    total_subjects = len(marks)
    cgpa = 0
    for mark in marks:
        if mark >= 85:
            gpa = 4.0
        elif mark >= 80:
            gpa = 3.8
        elif mark >= 75:
            gpa = 3.4
        elif mark >= 71:
            gpa = 3.0
        elif mark >= 68:
            gpa = 2.8
        elif mark >= 64:
            gpa = 2.4
        elif mark >= 61:
            gpa = 2.0
        elif mark >= 57:
            gpa = 1.8
        elif mark >= 53:
            gpa = 1.4
        elif mark >= 50:
            gpa = 1.0
        else:
            gpa = 0.0

        cgpa += gpa
    cgpa /= total_subjects
    return round(cgpa, 2)


filename = "marksheet.csv"

with open(filename, "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    marks = []
    for row in reader:
        mark = float(row[1])
        marks.append(mark)
cgpa = calculate_cgpa(marks)

print(f"CGPA: {cgpa}")
