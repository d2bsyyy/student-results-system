"""JSON file storage for student records."""
import json
from pathlib import Path
from student import Student

DATA_FILE = Path(__file__).parent / "data" / "students.json"

def load_students():
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        DATA_FILE.write_text("[]", encoding="utf-8")
        return []
    try:
        raw_data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return [Student.from_dict(item) for item in raw_data]
    except (json.JSONDecodeError, KeyError, TypeError) as error:
        raise RuntimeError(f"Could not read the student data file: {error}") from error

def save_students(students):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    temporary_file = DATA_FILE.with_suffix(".tmp")
    temporary_file.write_text(
        json.dumps([student.to_dict() for student in students], indent=4),
        encoding="utf-8"
    )
    temporary_file.replace(DATA_FILE)
