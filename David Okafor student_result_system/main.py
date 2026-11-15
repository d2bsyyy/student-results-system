"""Main menu for the Student Result Management System."""
from datetime import datetime
from student import Student
from results import SUBJECTS, record_scores, calculate_total, calculate_average, assign_grade
from storage import load_students, save_students
from reports import student_report, class_report, class_statistics, save_text_report

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")

def find_student(students, identifier):
    identifier = identifier.strip().lower()
    return next((s for s in students
                 if s.student_id.lower() == identifier
                 or s.full_name.lower() == identifier), None)

def add_student(students):
    print("\n--- Register a Student ---")
    student_id = get_non_empty("Student ID: ")
    if any(s.student_id.lower() == student_id.lower() for s in students):
        print("That Student ID is already registered.")
        return
    name = get_non_empty("Full name: ")
    class_form = get_non_empty("Class/Form: ")
    gender = get_non_empty("Gender: ")
    dob = get_non_empty("Date of birth (YYYY-MM-DD): ")
    try:
        datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        print("Invalid date. Please use YYYY-MM-DD.")
        return
    students.append(Student(student_id, name, class_form, gender, dob))
    save_students(students)
    print("Student registered successfully.")

def list_students(students):
    print("\n--- Registered Students ---")
    if not students:
        print("No students have been registered.")
        return
    for student in students:
        print(f"{student.student_id:<15} {student.full_name:<28} {student.class_form}")

def search_student(students):
    term = get_non_empty("Enter Student ID or exact name: ")
    student = find_student(students, term)
    if student:
        print(student_report(student))
    else:
        print("Student not found.")

def update_student(students):
    student = find_student(students, get_non_empty("Enter Student ID or exact name: "))
    if not student:
        print("Student not found.")
        return
    print("Press Enter to keep the current value.")
    for attribute, label in [
        ("full_name", "Full name"), ("class_form", "Class/Form"),
        ("gender", "Gender"), ("date_of_birth", "Date of birth (YYYY-MM-DD)")
    ]:
        new_value = input(f"{label} [{getattr(student, attribute)}]: ").strip()
        if new_value:
            if attribute == "date_of_birth":
                try:
                    datetime.strptime(new_value, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date; keeping the previous date.")
                    continue
            setattr(student, attribute, new_value)
    save_students(students)
    print("Student information updated.")

def delete_student(students):
    student = find_student(students, get_non_empty("Enter Student ID or exact name: "))
    if not student:
        print("Student not found.")
        return
    confirm = input(f"Delete {student.full_name}? (y/n): ").strip().lower()
    if confirm == "y":
        students.remove(student)
        save_students(students)
        print("Student record deleted.")
    else:
        print("Deletion cancelled.")

def enter_or_update_scores(students):
    student = find_student(students, get_non_empty("Enter Student ID or exact name: "))
    if not student:
        print("Student not found.")
        return
    print("Enter scores from 0 to 100.")
    new_scores = {}
    try:
        for subject in SUBJECTS:
            previous = student.scores.get(subject, "not entered")
            value = input(f"{subject} (current: {previous}): ").strip()
            if not value and subject in student.scores:
                new_scores[subject] = student.scores[subject]
            else:
                new_scores[subject] = float(value)
        record_scores(student, new_scores)
        save_students(students)
        print("Scores saved successfully.")
    except ValueError as error:
        print(f"Scores were not saved: {error}")

def show_results(students):
    print(class_report(students))

def show_statistics(students):
    print("\n--- Class Statistics ---")
    print(class_statistics(students))

def sort_students(students):
    print("1. Average score (highest to lowest)\n2. Name (A-Z)")
    choice = input("Choose sorting method: ").strip()
    if choice == "1":
        ordered = sorted(
            [s for s in students if s.scores],
            key=lambda s: calculate_average(s.scores), reverse=True
        )
    elif choice == "2":
        ordered = sorted(students, key=lambda s: s.full_name.lower())
    else:
        print("Invalid choice.")
        return
    if not ordered:
        print("No matching student records.")
    for student in ordered:
        if student.scores:
            print(f"{student.full_name} | Average: {calculate_average(student.scores):.2f} | Grade: {assign_grade(calculate_average(student.scores))}")
        else:
            print(f"{student.full_name} | Results not entered")

def save_report(students):
    content = class_report(students) + "\n\n" + class_statistics(students)
    path = save_text_report(content)
    print(f"Report saved to: {path}")

def main():
    try:
        students = load_students()
    except RuntimeError as error:
        print(error)
        return

    actions = {
        "1": lambda: add_student(students),
        "2": lambda: list_students(students),
        "3": lambda: search_student(students),
        "4": lambda: update_student(students),
        "5": lambda: delete_student(students),
        "6": lambda: enter_or_update_scores(students),
        "7": lambda: show_results(students),
        "8": lambda: show_statistics(students),
        "9": lambda: sort_students(students),
        "10": lambda: save_report(students)
    }
    while True:
        print("""
========================================
   STUDENT RESULT MANAGEMENT SYSTEM
========================================
1. Add a new student
2. View all students
3. Search for a student
4. Update student information
5. Delete a student
6. Enter / Update subject scores
7. View all student results
8. View class statistics
9. Sort students
10. Save class report to a text file
0. Exit
========================================""")
        choice = input("Enter your choice: ").strip()
        if choice == "0":
            save_students(students)
            print("Data saved. Thank you for using the system.")
            break
        action = actions.get(choice)
        if action:
            try:
                action()
            except (ValueError, OSError) as error:
                print(f"An error occurred: {error}")
        else:
            print("Invalid menu choice. Please try again.")

if __name__ == "__main__":
    main()
