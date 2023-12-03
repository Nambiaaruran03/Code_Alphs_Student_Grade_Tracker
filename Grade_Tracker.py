def get_subject_grades(subject_name):
    grades = []
    num_grades = int(input(f"How many grades for {subject_name}? "))
    
    for _ in range(num_grades):
        grade = float(input(f"Enter {subject_name} grade: "))
        grades.append(grade)
    
    return grades

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def main():
    num_subjects = int(input("How many subjects? "))
    
    subjects = []
    for i in range(1, num_subjects + 1):
        subject_name = input(f"Enter name for subject {i}: ")
        subject_grades = get_subject_grades(subject_name)
        subjects.append((subject_name, subject_grades))

    print("\nGrades Summary:")
    for subject_name, grades in subjects:
        average_grade = calculate_average(grades)
        print(f"{subject_name} - Grades: {grades}, Average: {average_grade:.2f}")

if __name__ == "__main__":
    main()
