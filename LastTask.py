#Бакиева Есфирь ПО-25-1
class Book:
    def __init__(self, name, author, year, status):
        self.name = name
        self.author = author
        self.year = year
        self.status = status

    @classmethod
    def from_string(cls, student_string):
        name, author, year, status  = student_string.split('-')
        return cls(name, author, int(year), status)

    def information(self):
        print(f"Название книги: {self.name}, Автор: {self.author}, Год издания: {self.year}, Статус: {self.status}")

    def statusbook(self):
        if self.status == "Доступна":
            self.status = "Выдана"
        else:
            self.status = "Доступна"

class PaperBook(Book):
    def __init__(self, name, author, year, status, pages):
        super().__init__(name, author, year, status) 
        self.pages = pages
    
    def information(self):
        print(f"Название книги: {self.name}, Автор: {self.author}, Год издания: {self.year}, Статус: {self.status}, Количество страниц: {self.pages}")

class EBook(Book):
    def __init__(self, name, author, year, status, filesize):
        super().__init__(name, author, year, status) 
        self.filesize = filesize
    
    def information(self):
        print(f"Название книги: {self.name}, Автор: {self.author}, Год издания: {self.year}, Статус: {self.status}, Размер файла: {self.filesize}")


class Library:
    def __init__(self):
        self.books = []

    def supplement(self, book):
        self.books.append(book)

    def delete(self, name):
        for g in self.books:
            if g.name == name:
                self.books.remove(g)

    def search(self, name):
        for i in self.books:
            if i.name == name:
                print(f"Книга найдена: {name}")
                return
        print("Книга не найдена")

    def show_all(self):
        for z in self.books:
            z.information()

    def issue(self, name):
        for f in self.books:
            if f.name == name:
                if f.status == "Доступна":
                    f.status = "Выдана"
                    print("Книга выдана")
                else:
                    print("Книга уже выдана")
                return
        print("Книга не найдена")

    def returnB(self, name):
        for f in self.books:
            if f.name == name:
                if f.status == "Выдана":
                    f.status = "Доступна"
                    print("Книга возвращена")
                else:
                    print("Книга уже находится в библиотеке")
                return
        print("Книга не найдена")














    
paper = PaperBook("Убийство в Восточном экспрессе", "Агата Кристи", 1934, "Доступна", 320)
ebook = EBook("Основание", "Айзек Азимов", 1951, "Выдана", 3.2)

paper.information()
ebook.information()