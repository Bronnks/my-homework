def calc_perc(num1: int, num2: int) -> int:
    return round((num1 / num2) * 100)


class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        if pages <= 0:
            raise ValueError
        self.pages = pages
        self.start_read = 0

    def read(self, pages: int):
        if self.start_read >= self.pages:
            print('Эту книгу вы уже полностью прочитали, начните читать другую книгу.')
        else:
            res = calc_perc(self.start_read + pages, self.pages)
            if res >= 100:
                print('Вы прочитали всю книгу.')
            else:
                print(f'Вы прочитали {res}% книги.')
            self.start_read += pages

    def read_info(self) -> int:
        res = calc_perc(self.start_read, self.pages)
        if res >= 100:
            return 100
        else:
            return res


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: object):
        self.books.append(book)

    def lib_info(self):
        for i in self.books:
            print(f'Книга {i.title} прочитана на {i.read_info()}%.')
