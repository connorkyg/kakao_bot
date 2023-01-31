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

    def get_authcode(self, kakaoid=None):
        method = 'GET'
        api = '/oauth/authorize'
        auth_code = f'./{kakaoid}_authorization_code.txt'
        if os.path.isfile(auth_code):
            with open(auth_code, 'r', encoding='utf-8') as f:
                return f.read()
        elif not os.path.isfile(auth_code):
            print("[INFO] Authorization code 발급이 필요합니다.")

            def get_authurl():
                params = {
                    'client_id': secrets.secret[f'{kakaoid}']['KEYS']['rest_api'],
                    'redirect_uri': secrets.secret[f'{kakaoid}']['URI']['redirect_uri'],
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

    def get_token(self, kakaoid=None):
        method = 'POST'
        api = '/oauth/token'
        access_token = f'./{kakaoid}_access_token.txt'
        baseurl = 'https://kauth.kakao.com'

        if os.path.isfile(access_token):
            with open(access_token, 'r') as f:
                token = f.read()
            return token
        elif not os.path.isfile(access_token):
            code = self.get_authcode(kakaoid=kakaoid)
            print("Access Token 발급이 필요합니다.")
            data = {
                'grant_type': 'authorization_code',
                'client_id': secrets.secret[f'{kakaoid}']['KEYS']['rest_api'],
                'redirect_uri': secrets.secret[f'{kakaoid}']['URI']['redirect_uri'],
                'code': code
            }
            response = requests.request(method=method, url=baseurl + api, data=data)
            if 'error' in response.json():
                print(response.json())
                exit()
            elif not 'error' in response.json():
                token = response.json()['access_token']
                print(token)
                with open(access_token, 'w+') as f:
                    f.write(token)
                return token


if __name__ == '__main__':
    # todo: 2023-01-30
    # todo: browser 클래스 추상화/캡슐화
    # todo: Access Token 발급 부분 수정 및 고도화 필요
    acnt1 = auth()
    acnt2 = auth()
    acnt1.get_token('vlrrkem')
    acnt2.get_token('youngkht1')
