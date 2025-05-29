class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Membership ID: {self.member_id}")


class StudentMember(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.borrowed_books = 0

    def add_book(self):
        self.borrowed_books += 1
        print(f"Book borrowed. Total books now: {self.borrowed_books}")

    def return_book(self):
        if self.borrowed_books > 0:
            self.borrowed_books -= 1
            print(f"Book returned. Total books now: {self.borrowed_books}")
        else:
            print("No books to return.")

    def display_status(self):
        self.display_info()
        print(f"Books currently borrowed: {self.borrowed_books}")


# Example usage
if __name__ == "__main__":
    student = StudentMember("Alice", "S123")
    student.display_status()
    student.add_book()
    student.add_book()
    student.return_book()
    student.display_status()