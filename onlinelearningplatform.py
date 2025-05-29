class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")


class Instructor(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
        self.contents = []

    def upload_content(self, content):
        self.contents.append(content)

    def display_info(self):
        super().display_info()
        print(f"Role: Instructor")
        print(f"Subject: {self.subject}")
        print(f"Contents: {self.contents}")


class CourseCreator(Instructor):
    def __init__(self, name, email, subject):
        super().__init__(name, email, subject)
        self.courses = {}

    def create_course(self, course_name, modules):
        self.courses[course_name] = modules

    def display_info(self):
        super().display_info()
        print(f"Role: Course Creator")
        print(f"Courses: {self.courses}")


# Example usage
user = User("Alice", "alice@example.com")
instructor = Instructor("Bob", "bob@example.com", "Math")
creator = CourseCreator("Charlie", "charlie@example.com", "Programming")

instructor.upload_content("Algebra Notes")
creator.upload_content("Python Basics")
creator.create_course("Python 101", ["Intro", "Variables", "Loops"])

print("\nUser Info:")
user.display_info()

print("\nInstructor Info:")
instructor.display_info()

print("\nCourse Creator Info:")
creator.display_info()