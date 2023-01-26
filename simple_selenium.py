import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import subprocess
import chromedriver_autoinstaller


class browser:
    def __init__(self):
        # 현재 크롬 버전 체크 & 업데이트 진행
        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
        path = f'./{chrome_ver}/chromedriver.exe'
        if os.path.isfile(path):
            pass
        elif not os.path.isfile(path):
            chromedriver_autoinstaller.install(True)
        # subprocess.Popen(
        #     r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')  # 디버거 크롬 구동
        # self.path = r"D:/Development/Python/Coupang Partners/utils/chromedriver.exe"
        self.USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f'user-agent={self.USER_AGENT}')
        self.options.add_argument("lang=dko_KR")
        self.driver = webdriver.Chrome(service=Service(path), options=self.options)
        # self.driver = webdriver.Chrome(service=Service(self.path), options=self.options)
