from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Crawler:

    def __init__(self):
        pass

    def selenium_exit(self):
        pass

    def movetosite(self,address):
        print(address)
        pass

    def object_selection(self):
        pass

    
    def object_click(self):
        pass

    def scrolling(self):
        pass


    def screencapture(self, i):
        options = webdriver.ChromeOptions()  # instance of ChromeOptions WebDriver가 설치됨.
        
        # headless 옵션 설정
        # options.add_argument('headless') #브라우저가 눈에 안보이게 됨. 만들어가는 과정에는 절차를 봐야해서 이 옵션을 끔.
        options.add_argument("no-sandbox")  #

        # 브라우저 윈도우 사이즈
        options.add_argument('window-size=1920x1080')  # 디스플레이 해상도 설정에서 확인.

        # 사람처럼 보이게 하는 옵션들
        options.add_argument("disable-gpu")  # 가속 사용 x
        options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
        options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

        # 드라이버 서비스 설정
        service = Service('./chromedriver.exe')
        
        # 드라이버 초기화
        driver = webdriver.Chrome(service=service, options=options)

        driver.get('http://blog.naver.com/hariver1220')
        driver.implicitly_wait(1) #접속한 후 잠시 멈춤
        driver.save_screenshot(f'capture{i}.png')  # 화면캡처

        driver.quit()  # driver 종료




def main():
    crawl = Crawler()
    crawl.movetosite('http://blog.naver.com/hariver1220')
    for i in range(3):  # 반복 횟수 지정
        crawl.screencapture(i)

if __name__ == "__main__":
    #scheduler -> while문으로 돌면서 작업해야하면 main() 호출
    main()
