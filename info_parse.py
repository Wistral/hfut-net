from os import path


def parse_headers(raw: str):
    raw = raw.split('\n')[1:-1]
    raw = [_.split(': ')for _ in raw]
    headers ={}
    for _ in raw:
        headers[_[0]] = _[1]
    return headers


def parse_data(raw: str):
    raw = raw.split('\n')[1:-1]
    raw = [_.split(': ') for _ in raw]
    headers = {}
    for _ in raw:
        headers[_[0]] = _[1]
    return headers


def login():
    file = './info.txt'
    if path.exists(file) and path.getsize(file):
        with open(file, 'r') as f:
            ans = [_[:-1]for _ in f.readlines()]
            return ans
    else:
        with open(file, 'w') as f:
            account = input('请输入学号/帐号:\n')
            password = input('请输入密碼:\n')
            f.write(account+'\n')
            f.write(password+'\n')
            return account, password
