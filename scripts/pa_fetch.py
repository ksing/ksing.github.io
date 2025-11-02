import os
import requests

username = 'KushS'


if __name__ == '__main__':
    response = requests.get(
        f'https://eu.pythonanywhere.com/api/v0/user/{username}/cpu/',
        headers={'Authorization': f'Token {os.environ["PYTHONANYWHERE_API"]}'}
    )
    if response.status_code == 200:
        print('CPU quota info:\n', response.content)
    else:
        print(f"Got unexpected status code {response.status_code}: {response.content!r}")
