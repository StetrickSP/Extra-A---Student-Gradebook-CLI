import json
import os

# courses = {
#     'AU003': {'name': 'English 1', 'credits': 3, 'semester': 3, 'score': 71},
#     'MA101': {'name': 'Calculus I', 'credits': 4, 'semester': 1, 'score': 85},
#     'CS102': {'name': 'Programming Basics', 'credits': 3, 'semester': 1, 'score': 92},
#     'PH103': {'name': 'Physics I', 'credits': 4, 'semester': 1, 'score': 76},
#     'EC201': {'name': 'Microeconomics', 'credits': 3, 'semester': 2, 'score': 88},
#     'ST202': {'name': 'Statistics', 'credits': 3, 'semester': 2, 'score': 81},
#     'EN204': {'name': 'English 2', 'credits': 3, 'semester': 2, 'score': 67},
#     'MA203': {'name': 'Calculus II', 'credits': 4, 'semester': 2, 'score': 90},
#     'CS301': {'name': 'Data Structures', 'credits': 4, 'semester': 3, 'score': 94},
#     'PH302': {'name': 'Physics II', 'credits': 3, 'semester': 3, 'score': 78},
# }

DATA_FILE = "gradebook.json"

def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(courses, f, indent=4)
    print(f"Data saved to {DATA_FILE}.")

def load_data():
    """Load course data from JSON file if it exists."""
    global courses
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            courses = json.load(f)
        print(f"Loaded data from {DATA_FILE}.")
    else:
        courses = {}
        print("No existing data file found — starting fresh.")



# helper functions
def add_course(code, name, credits: int, semester: int, score: float):
    courses[code] = {'name':name, 'credits':int(credits), 'semester': int(semester), 'score': float(score)}
    save_data()
    print(f'Added course code {code} as {name}, credits: {credits}, semester: {semester}, score: {score}')

def update_course(code):
    try:
        if code in courses:
            info = courses[code]
            print(f'\nCourse code: {code}')
            print(f"  1. name: {info['name']}")
            print(f'  2. credits: {info['credits']}')
            print(f'  3. semester: {info['semester']}')
            print(f'  4. score: {info['score']}')
        else:
            print("Course not found.")
            return

        option = input("Choose the info you want to change (by number), type 'Quit' to exit: ")
        while option != "Quit":
            if option == "1": 
                new_name = input("Type in the new course name: ")
                courses[code]['name'] = new_name
                print(f"Changed name into {new_name}")
            elif option == "2":
                new_credits = input("Type in the new course credits: ")
                courses[code]['credits'] = new_credits
                print(f"Changed credits into {new_credits}")
            elif option == "3":
                new_semester = input("Type in the new course semester: ")
                courses[code]['semester'] = new_semester
                print(f"Changed semester into {new_semester}")
            elif option == "4":
                new_score = input("Type in the new course score: ")
                courses[code]['score'] = new_score
                print(f"Changed credits into {new_score}")
            else: 
                print("Error")
                break
            save_data()
            option = input("Choose the info you want to change (by number), type 'Quit' to exit: ")

    except KeyError: 
        print("Error. No courses found.")


def delete_course(code):
    try:
        courses.pop(code)
        save_data()
        print(f"Course {code} deleted sucessfully!")
    except KeyError:
        print("Error. No courses found.")
  

def view_book(data):
    option = input("Type 'Quit' to exit, or press Enter to see gradebook: ")
    while option != "Quit":
        print("\n----- Courses details -----")
        print(f"{'Code':<8} {'Name':<20} {'Credits':<8} {'Semester':<10} {'Score':<6}")
        print("-" * 55)
        for code, info in data.items():
            print(f"{code:<8} {info['name']:<20} {info['credits']:<8} {info['semester']:<10} {info['score']:<6}")

        print("-" * 55)
        option = input("Type 'Quit' to exit, or press Enter to see gradebook: ")

def calc_GPA_by_semester(semester: int) -> float:
    semester_courses = [c for c in courses.values() if c['semester'] == semester]
    if not semester_courses:
        print(f"No courses found for semester {semester}.")
        return 0.0

    total_points = sum(c['score'] * c['credits'] for c in semester_courses)
    total_credits = sum(c['credits'] for c in semester_courses)
    gpa = total_points / total_credits
    print(f"GPA for semester {semester}: {gpa:.2f}")
    return gpa

def calc_overall_GPA() -> float:
    total_points = sum(c['score'] * c['credits'] for c in courses.values())
    total_credits = sum(c['credits'] for c in courses.values())
    gpa = total_points / total_credits
    print(f"Overall GPA: {gpa:.2f}")
    return gpa


# helper functions

def main():
    load_data()

    print("\n-------- Welcome to the Student Gradebook! --------")
    print("1. Add course")
    print("2. Update course")
    print("3. Delete course")
    print("4. View gradebook")
    print("5. Calculate GPA")
    print("6. Exit gradebook")

    choice = input("Choose an option: ")

    if choice == "1":
        code = input("Enter course code to add: ")
        if code in courses:
            print("There is already a course with that code.")
            main()
        name = input("Enter course name: ")
        credits = input("Enter credits need to be taken: ")
        semester = input("Enter the semester the course will take place: ")
        score = input("Enter the score of the course (if there is): ")
        add_course(code, name, credits, semester, score)
        main()

    elif choice == "2":
        code = input("Enter course code to update: ")
        update_course(code)
        main()

    elif choice == "3":
        code = input("Enter course code to delete: ")
        delete_course(code)
        main()

    elif choice == "4": 
        view_book(courses)
        main()

    elif choice == "5": 
        option = input("Would you like to continue? Type 'Quit' to exit, press Enter to continue: ")
        semester = int(input("Enter the semester you want to calculate the semester for: "))
        while option != "Quit":
            calc_GPA_by_semester(semester)
            calc_overall_GPA()
            option = input("Would you like to continue? Type 'Quit' to exit, press Enter to continue: ")
            if option == "Quit": break
            semester = int(input("Enter the semester you want to calculate the semester for: "))
        main()

    elif choice == "6":
        save_data()
        print("Bye! Have a great day!")
        exit()

    else:
        print("Please choose a valid option.")
        main()


if __name__ == '__main__':
    main()