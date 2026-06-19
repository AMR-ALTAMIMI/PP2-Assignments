# Registration system

def register_student(*courses, **student_info):
    print("Student Information:")

    for key, value in student_info.items():
        print(f"{key}: {value}")

    print("\nCourses:")

    for course in courses:
        print(course)

register_student(
    "Python",
    "Mathematics",
    "Physics",
    name="Ahmed",
    age=20,
    university="KazNU"
)
