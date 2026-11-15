# Student Result Management System

## Project information
- **Project:** Design, Develop and Document a Student Result Management System using Python
- **Course:** Introduction to Python Programming
- **Project type:** Individual practical project
- **Storage:** JSON (`data/students.json`)
- **Interface:** Menu-driven command-line application

## Features
1. Register students with ID, name, class/form, gender and date of birth.
2. View, search, update and delete student records.
3. Enter or update scores in five subjects: English, Mathematics, Biology, Chemistry and Physics.
4. Calculate total, average and grade.
5. View individual report cards and class result summaries.
6. Sort results by average (highest first) or students by name.
7. Display highest average, lowest average and class average.
8. Save a text report to `class_report.txt`.
9. Automatically save and load records using JSON.

## Grading scale
- A: 70–100
- B: 60–69.99
- C: 50–59.99
- D: 45–49.99
- F: Below 45

This is the grading scale configured in `results.py`. Change it if your lecturer or school specifies another scale.

## Requirements
- Python 3.8 or newer
- No third-party packages are required.

## How to run
1. Download or clone this project.
2. Open a terminal or command prompt in the `student_result_system` folder.
3. Run:

   ```bash
   python main.py
   ```

   On some computers, use `python3 main.py`.

4. Select an option from the menu.
5. Register a student before entering that student's scores.

## Project structure

```text
student_result_system/
├── main.py
├── student.py
├── results.py
├── storage.py
├── reports.py
├── data/
│   └── students.json
└── README.md
```

## Python concepts demonstrated
- Variables, strings, numbers, dictionaries and lists
- `if`, `elif`, `else`, `for` and `while`
- Functions with parameters and return values
- A `Student` class and object-oriented programming
- Sorting with `sorted()` and `lambda`
- JSON file reading and writing
- Exception handling with `try` and `except`
- Date validation and result-entry timestamps using `datetime`
- Modules and imports

## Important notes
- Student IDs must be unique.
- Scores must be between 0 and 100.
- At least five subject scores are required for a result.
- Data is stored locally in `data/students.json`.
- Keep a backup of the JSON file before manually editing it.

## GitHub upload guide
Create a repository named `student-result-system`, then run these commands in this project folder:

```bash
git init
git add .
git commit -m "Create student result management system"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/student-result-system.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username. For your assignment, make regular commits as you develop and test the project, rather than making only one final commit.
