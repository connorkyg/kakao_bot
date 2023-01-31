data = {
    'grant_type': 'authorization_code',
    'client_id': secrets.KEYS['rest_api'],
    'client_id': secrets.secret[f'{kakaoid}']['KEYS']['rest_api'],
    'redirect_uri': secrets.URI['redirect_uri'],
    'redirect_uri': secrets.secret[f'{kakaoid}']['KEYS']['redirect_uri'],
    'code': self.get_authcode()
}


def get_authurl():
    params = {
        'client_id': f"{secrets.KEYS['rest_api']}",
        'redirect_uri': f"{secrets.URI['redirect_uri']}",
        'response_type': 'code'
    }