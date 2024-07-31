from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import polars as pl

chrome_driver = r"C:\dev\mysite\chromedriver.exe"


class Crawling:
    def __init__(self, mode="new"):
        self.chrome_driver = chrome_driver
        self.chrome_options = Options()
        if mode == "new":
            self.browser = webdriver.Chrome(options=self.chrome_options)
        else:
            pass
        self.browser.maximize_window()
        print("브라우저작동됨")

    def 이미지링크추출(self, xpath, attr):
        결과들 = []
        for i in range(0, 17):
            결과들.append(
                self.browser.find_elements(By.XPATH, xpath)[i].get_attribute(attr)
            )
        결과들.pop()
        return 결과들

    def 날짜추출(self, xpath):
        # //*[contains(concat( " ", @class, " " ), concat( " ", "doodle-card-content__date", " " ))]
        결과들 = []
        for i in range(0, 16):
            결과들.append(self.browser.find_elements(By.XPATH, xpath)[i].text)
        return 결과들

    def 타이틀추출(self, xpath):
        # //*[contains(concat( " ", @class, " " ), concat( " ", "doodle-card-content__event", " " ))]
        결과들 = []
        for i in range(0, 16):
            결과들.append(self.browser.find_elements(By.XPATH, xpath)[i].text)
        return 결과들

    def 객체클릭(self, xpath):
        # print(self.browser.find_elements(By.XPATH, xpath)[0])
        self.browser.find_elements(By.XPATH, xpath)[0].click()

    def 화면스크롤아래로(self):
        pass

    def 사이트로이동(self, addr):
        self.browser.get(addr)

    def 셀레니움종료(self):
        driver.get("https://naver.com")
        driver.implicitly_wait(3)
        driver.get_screenshot_as_file("capture_naver.png")  # 화면캡처

        driver.quit()  # driver 종료

    def 잠시대기(self, second):
        import time

        time.sleep(second)


def main():
    crawling = Crawling("new")
    crawling.사이트로이동("https://google.com")
    crawling.잠시대기(6)
    crawling.객체클릭(
        "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[2]"
    )
    crawling.잠시대기(3)
    crawling.객체클릭('//*[@id="section-1"]/div/div/div[1]/div[2]/div/span[1]/a')
    crawling.잠시대기(4)
    이미지링크들 = crawling.이미지링크추출("//img", "src")
    날짜들 = crawling.날짜추출(
        '//*[contains(concat( " ", @class, " " ), concat( " ", "doodle-card-content__event", " " ))]'
    )
    타이틀들 = crawling.타이틀추출(
        '//*[contains(concat( " ", @class, " " ), concat( " ", "doodle-card-content__event", " " ))]'
    )    

    df = pl.DataFrame(
        {
            "이미지링크들": 이미지링크들,
            "날짜들": 날짜들,
            "타이틀들": 타이틀들,
        }
    )

    df.write_excel(column_totals=True, autofit=True)
    # df = pd.DataFrame(data=zip(이미지링크들,날짜들,타이틀들), columns=["이미지링크들","날짜들","타이틀들",])
    # df.to_excel("asdf.xlsx")


if __name__ == "__main__":
    # 스캐줄러
    main()