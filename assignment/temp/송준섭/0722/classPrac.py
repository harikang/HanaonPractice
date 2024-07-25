class Page:
    book_title = "Python Practice Book"

    def __init__(self, num, content):
        self.num = num
        self.content = content

    def output(self):
        return f"{self.content}"

    @classmethod
    def print_page(cls, *pages):
        print(cls.book_title)
        pages = list(pages)
        for page in pages:
            print(page.output())
