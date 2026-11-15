"""Score validation, calculations and grading rules."""
from datetime import datetime

SUBJECTS = ["English", "Mathematics", "Biology", "Chemistry", "Physics"]

def validate_score(value):
    score = float(value)
    if not 0 <= score <= 100:
        raise ValueError("A score must be between 0 and 100.")
    return score

def calculate_total(scores):
    return sum(float(score) for score in scores.values())

def calculate_average(scores):
    if not scores:
        return 0.0
    return calculate_total(scores) / len(scores)

def assign_grade(average):
    # Grading scale used by this project; confirm with your lecturer if your
    # school uses a different grading scale.
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    else:
        return "F"

def record_scores(student, scores):
    if len(scores) < 5:
        raise ValueError("At least five subject scores are required.")
    student.scores = {subject: validate_score(score) for subject, score in scores.items()}
    student.result_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
