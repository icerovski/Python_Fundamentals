# Add to Book to database if it is VALID, else raise exception and don't add

# title
# chapters [] = len(chapters) > 1
# author = must be str
# pages = must be int
# pub_date = dd-mm-yyyy

# Book examples
"""
Title1 Author 5 22-5-1998 1,2,3
Title2 Author2 5 22-5-1998 1,2,3
Title4 Author3 10 22/5/1998 1,2,3
Title3 Author4 6 22-5-1998 1,2,3,4,5
end

"""

# Sort: len of chap descending, then by name ascending

class Book:
    def __init__(self, title, author, pages, pub_date, chapters):
        self.title = title
        self.author = self.set_author(author)
        self.pages = self.set_pages(pages)
        self.pub_date = self.set_pub_date(pub_date)
        self.chapters = self.set_chapters(chapters)


    def set_author(self, author):
        if isinstance(author, str):
            return author
        else: raise Exception

    def set_pages(self, pages):
        if isinstance(pages, int):
            return pages
        else: raise Exception

    def set_pub_date(self, pub_date):
        l = len(list(pub_date.split('-')))
        if l == 3:
            return pub_date
        else: raise Exception

    def set_chapters(self, chapters):
        c = len(list(chapters.split(',')))
        if c >= 3:
            return chapters
        else: raise Exception


data = input()
books = []

while not data == 'end':
    title, author, pages, pub_date, chapters = list(data.split())

    try:
        book = Book(title, author, int(pages), pub_date, chapters)
        books.append(book)
    except:
        print('data invalid')

    data = input()


formatted_data = sorted(books, key= lambda obj: (-len(obj.chapters), obj.title))

for book in formatted_data:
    print(f"{book.title} --> chapters --> {book.chapters}")
