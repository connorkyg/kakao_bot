import json
import requests

# api = Message(service_key=secrets.KEYS["restApi"])
# auth_url = api.get_url_for_generating_code()
# print(auth_url)

# TODO: py 파일로 저장하지 않으며, 매번 read 하지않을 수 있는 방법 고안
path = './access_token.txt'
with open(path, 'r+', encoding='utf-8') as f:
    ACCESS_TOKEN = json.loads(f)['access_token']


class apis:
    def __init__(self):
        self.method = None
        self.baseurl = None
        self.api_talktome = None

    def talk_memo_default_send(self):
        self.method = 'POST'
        self.baseurl = 'https://kapi.kakao.com/v2/api/'
        self.api_talktome = 'talk/memo/default/send'
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
            'link': self.link,
            'button_title': '버튼 타이틀 테스트'
        }

        '''
        curl -v -X POST "https://kapi.kakao.com/v2/api/talk/memo/default/send" \
            -H "Content-Type: application/x-www-form-urlencoded" \
            -H "Authorization: Bearer ${ACCESS_TOKEN}" \
            --data-urlencode 'template_object={
                "object_type": "text",
                "text": "텍스트 영역입니다. 최대 200자 표시 가능합니다.",
                "link": {
                    "web_url": "https://developers.kakao.com",
                    "mobile_web_url": "https://developers.kakao.com"
                },
                "button_title": "바로 확인"
            }'

        '''
        requests.request(method=self.method, url=self.baseurl + self.api_talktome, headers=headers, data=data)
