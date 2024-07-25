class Page:
    book_title = 'Python Practice Book'
    def __init__(self, num, content):
        self.num = num
        self.content = content
    def output(self):
        return f'{self.content}'
    # 클래스 메서드의 첫 번째 인수는 클래스 객체
    @classmethod
    def print_pages(cls, *pages):
        # 클래스 객체 이용
        print(cls.book_title)
        pages = list(pages)
        # 페이지 순으로 정렬해서 출력
        for page in sorted(pages, key=attrgetter('num')):
            print(page.output())



class Page:
    def __init__(self, num, content):
        self.num = num
        self.content = content
    @staticmethod  # 스태틱 메서드로 정의
    def check_blank(page):
        return bool(page.content)