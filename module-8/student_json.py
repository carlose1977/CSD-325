"""
---

# CSD325-T301 - Week 8.2 Assignment: JSON

---

**Professor**: John Woods<br>
**@Copyright**: BELLEVUE.edu<br>
**Modified By**: Carlos E. Escamilla<br>
**Email**: CEEscamilla@my365.BELLEVUE.edu<br>
**OS**: Windows 11 x64<br>
**Processor**: i9-13900<br>
**GPU**: NVIDIA GeForce RTX 3060<br>
**IDE**: DataSpell 2025.2<br>
**Interpreter**: Python 3.12<br>
**Libraries Managed by**: Miniforge3

---

**Version**:
- 1.0.0 - 2025.09.08 Week1: Programming Logic
- 1.0.1 - 2025.09.15 Week2: Documenting Debugging
- 1.0.2 - 2025.09.22 Week3: Brownfield Development
- 1.0.3 - 2025.09.29 Week4: CSV Read and Matplotlib
- 1.0.4 - 2025.10.06 Week5: Forest Fire Simulation 1
- 1.0.5 - 2025.10.13 Week6: Forest Fire Simulation 2
- 1.0.6 - 2025.10.20 Week7: Test Cases
- 1.0.7 - 2025.10.27 Week8: JSON Practice

**Description**:
This program demonstrates working with JSON data by:
1. Loading student data from a JSON file
2. Displaying the original student list
3. Adding a new student to the list
4. Displaying the updated student list
5. Writing the updated data back to the JSON file

"""

import json


def print_student_list(students):
    """
    Print formatted student information from the student list.

    Args:
        students (list): List of student dictionaries
    """
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")


def main():
    """Main program execution."""

    # File path for the JSON file
    json_file = "student.json"

    # Load the JSON file into a Python list
    print("Loading student data from JSON file...\n")
    with open(json_file, 'r') as file:
        student_list = json.load(file)

    # Display the original student list
    print("=" * 50)
    print("ORIGINAL STUDENT LIST")
    print("=" * 50)
    print_student_list(student_list)
    print()

    # Add a new student to the list
    new_student = {
        "F_Name": "Carlos",
        "L_Name": "Escamilla",
        "Student_ID": 99999,
        "Email": "CEscamilla@gmail.com"
    }

    student_list.append(new_student)

    # Display the updated student list
    print("=" * 50)
    print("UPDATED STUDENT LIST")
    print("=" * 50)
    print_student_list(student_list)
    print()

    # Write the updated list back to the JSON file
    with open(json_file, 'w') as file:
        json.dump(student_list, file, indent=4)

    print("=" * 50)
    print("The student.json file has been successfully updated!")
    print("=" * 50)


if __name__ == "__main__":
    main()


