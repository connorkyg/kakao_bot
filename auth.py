import os
import time
import json
import requests
from selenium.webdriver.common.by import By

from simple_selenium import browser
import secrets

driver = browser().driver


class auth(browser):
    def __init__(self):
        self.baseurl = 'https://kauth.kakao.com'

    def get_authcode(self):
        method = 'GET'
        api = '/oauth/authorize'
        auth_code = './authorization_code.txt'
        if os.path.isfile(auth_code):
            with open(auth_code, 'r', encoding='utf-8') as f:
                return f.read()
        elif not os.path.isfile(auth_code):
            print("[INFO] Authorization code 발급이 필요합니다.")

            def get_authurl():
                params = {
                    'client_id': f"{secrets.KEYS['rest_api']}",
                    'redirect_uri': f"{secrets.URI['redirect_uri']}",
                    'response_type': 'code'
                }
                response = requests.request(method=method, url=self.baseurl + api, params=params)
                return response.url

            driver.get(get_authurl())
            driver.find_element(By.XPATH, '//*[@id="input-loginKey"]').send_keys(input("ID 입력: "))
            driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys(input("PW 입력: "))
            driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
            time.sleep(3)
            code = driver.current_url.split('=')[1]
            with open(auth_code, 'w+', encoding='utf-8') as f:
                f.write(code)
            return code

    def get_token(self):
        method = 'POST'
        api = '/oauth/token'
        access_token = './access_token.txt'
        if os.path.isfile(access_token):
            with open(access_token, 'r') as f:
                token = f.read()
            return token
        elif not os.path.isfile(access_token):
            print("Access Token 발급이 필요합니다.")
            data = {
                'grant_type': 'authorization_code',
                'client_id': secrets.KEYS['rest_api'],
                'redirect_uri': secrets.URI['redirect_uri'],
                'code': self.get_authcode()
            }
            response = requests.request(method=method, url=self.baseurl + api, data=data)
            with open(access_token, 'w+') as f:
                f.write(response.json()['access_token'])
            return response.json()['access_token']
            # driver.get(response.url)
            # driver.find_element(By.XPATH, '//*[@id="input-loginKey"]').send_keys(input("ID 입력: "))
            # driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys(input("PW 입력: "))
            # driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()

            # if not 'error' in token:
            #     with open(access_token, 'w+') as f:
            #         json.dump(token, f)
            #     return token
            # else:
            #     print(token)


if __name__ == '__main__':
    # todo: 2023-01-30
    # todo: browser 클래스 추상화/캡슐화
    # todo: Access Token 발급 부분 수정 및 고도화 필요
    auth().get_token()