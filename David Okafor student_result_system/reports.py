"""Functions for displaying and saving student reports."""
from datetime import datetime
from results import calculate_total, calculate_average, assign_grade

def student_report(student):
    lines = [
        "=" * 48,
        "             STUDENT REPORT CARD",
        "=" * 48,
        f"Student ID:       {student.student_id}",
        f"Full Name:        {student.full_name}",
        f"Class/Form:       {student.class_form}",
        f"Gender:           {student.gender}",
        f"Date of Birth:    {student.date_of_birth}",
        "-" * 48,
        "SUBJECT SCORES"
    ]
    if student.scores:
        for subject, score in student.scores.items():
            lines.append(f"{subject:<25} {float(score):>7.2f}")
        total = calculate_total(student.scores)
        average = calculate_average(student.scores)
        lines += [
            "-" * 48,
            f"Total Score:      {total:.2f}",
            f"Average Score:    {average:.2f}",
            f"Grade:            {assign_grade(average)}",
            f"Result Entered:   {student.result_date or 'Not recorded'}"
        ]
    else:
        lines.append("No scores have been entered for this student.")
    lines.append("=" * 48)
    return "\n".join(lines)

def class_report(students):
    assessed = [s for s in students if s.scores]
    lines = ["STUDENT RESULT SUMMARY", "=" * 75,
             f"{'ID':<12}{'NAME':<25}{'TOTAL':>10}{'AVERAGE':>12}{'GRADE':>10}",
             "-" * 75]
    for student in sorted(assessed, key=lambda s: calculate_average(s.scores), reverse=True):
        average = calculate_average(student.scores)
        lines.append(
            f"{student.student_id:<12}{student.full_name[:24]:<25}"
            f"{calculate_total(student.scores):>10.2f}{average:>12.2f}"
            f"{assign_grade(average):>10}"
        )
    if not assessed:
        lines.append("No student results are available yet.")
    lines.append("=" * 75)
    return "\n".join(lines)

def class_statistics(students):
    assessed = [s for s in students if s.scores]
    if not assessed:
        return "No results are available for class statistics."
    averages = [calculate_average(s.scores) for s in assessed]
    return (
        f"Students with results: {len(assessed)}\n"
        f"Highest average:       {max(averages):.2f}\n"
        f"Lowest average:        {min(averages):.2f}\n"
        f"Class average:         {sum(averages) / len(averages):.2f}"
    )

def save_text_report(content, filename="class_report.txt"):
    report_path = __import__("pathlib").Path(__file__).parent / filename
    report_path.write_text(content, encoding="utf-8")
    return report_path
