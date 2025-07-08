import csv


def calculate_cgpa(marks):
    total_subjects = len(marks)
    if total_subjects == 0:
        return 0.0
        
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
    next(reader)  # Skip header row
    marks = []
    total_subjects = 0
    subjects_with_marks = 0
    
    for row in reader:
        total_subjects += 1
        # Check if row has at least 2 columns and the mark is not empty
        if len(row) >= 2 and row[1].strip():
            try:
                mark = float(row[1].strip())
                marks.append(mark)
                subjects_with_marks += 1
            except ValueError:
                # Skip invalid marks (non-numeric values)
                print(f"Warning: Invalid mark '{row[1]}' for subject '{row[0]}' - skipping")
                continue

if marks:
    cgpa = calculate_cgpa(marks)
    print(f"CGPA: {cgpa}")
    print(f"Calculated from {subjects_with_marks} subjects out of {total_subjects} total subjects")
else:
    print("No valid marks found in the CSV file. Please add your marks to calculate CGPA.")
