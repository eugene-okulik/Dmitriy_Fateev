class Book:
    page_material = "бумага"
    has_text = True

    def __init__(self, name, author, page_count, isbn, reserved=False):
        self.name = name
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = reserved

    def __str__(self):
        info = f"Название: {self.name}, Автор: {self.author}, страниц: {self.page_count}, материал: {self.page_material}"
        if self.reserved:
            info += ", зарезервирована"
        return info


class SchoolBook(Book):
    def __init__(self, name, author, page_count, isbn, subject, grade, has_tasks, reserved=False):
        super().__init__(name, author, page_count, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.has_tasks = has_tasks

    def __str__(self):
        info = f"Название: {self.name}, Автор: {self.author}, страниц: {self.page_count}, предмет: {self.subject}, класс: {self.grade}"
        if self.reserved:
            info += ", зарезервирована"
        return info


book1 = Book("Идиот", "Достоевский", 500, "978-5-17-123456-7")
book2 = Book("Война и мир", "Толстой", 1300, "978-5-17-123456-8")
book3 = Book("Преступление и наказание", "Достоевский", 600, "978-5-17-123456-9")
book4 = Book("Мастер и Маргарита", "Булгаков", 450, "978-5-17-123457-0")
book5 = Book("1984", "Оруэлл", 320, "978-5-17-123457-1")
book5.reserved = True

print(book1)
print(book2)
print(book3)
print(book4)
print(book5)

school1 = SchoolBook("Алгебра", "Иванов", 200, "978-5-17-123457-2", "Математика", 9, True)
school2 = SchoolBook("Геометрия", "Петров", 180, "978-5-17-123457-3", "Математика", 9, True)
school3 = SchoolBook("История России", "Сидоров", 250, "978-5-17-123457-4", "История", 10, False)
school4 = SchoolBook("География", "Кузнецов", 220, "978-5-17-123457-5", "География", 8, True)
school5 = SchoolBook("Физика", "Смирнов", 300, "978-5-17-123457-6", "Физика", 11, True)
school1.reserved = True

print()
print(school1)
print(school2)
print(school3)
print(school4)
print(school5)
