class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


def main():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course: ")

    student = Student(name, age, course)
    student.display_details()


if __name__ == "__main__":
    main()