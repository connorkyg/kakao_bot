import json
import requests


# TODO: py 파일로 저장하지 않으며, 매번 read 하지않을 수 있는 방법 고안
path = './access_token.txt'
with open(path, 'r+', encoding='utf-8') as f:
    ACCESS_TOKEN = f.read()


class apis:
    def talk_memo_default_send(self):
        method = 'POST'
        baseurl = 'https://kapi.kakao.com/v2/api/'
        api_talktome = 'talk/memo/default/send'
        headers = {
            'Authorization': f'Bearer {ACCESS_TOKEN}'
        }
        link = {
            'web_url': 'https://developers.kakao.com',
            'mobile_web_url': 'https://developers.kakao.com'
        }
        data = {
            'object_type': 'text',
            'text': 'test',  # todo: input("Message 입력: ")
            'link': link,
            'button_title': '버튼 타이틀 테스트'
        }
        response = requests.request(method=method, url=baseurl + api_talktome, headers=headers, data=data)
        return response


if __name__ == '__main__':
    test = apis()
    print(test.talk_memo_default_send().status_code)
    print(test.talk_memo_default_send().text)
    print(test.talk_memo_default_send().json())
