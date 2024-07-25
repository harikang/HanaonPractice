# 클래스 정의
class Page:
    def __init__(self, num, content, section=None):
        self.num = num
        self.content = content
        self.section = section
    def output(self):
        return f'{self.content}'
