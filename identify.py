import requests
from bs4 import BeautifulSoup
from os import path
import getpass
import subprocess
import sys


# user-info file name
USER_INFO_CONF = 'info.dat'


def is_connected():
    """
    test connectibility to Internet
    """
    try:
        code = subprocess.check_call(['ping', 'baidu.com', '-c 1', '-W 1'],
                                     stdout=subprocess.PIPE)
    except subprocess.CalledProcessError:
#        print('catch error!')
        return False
        pass
    return True


def login(store=True) -> (str, str):
    """
    get account and password
    It will ask for account and password and stored on first time.
    
    \param store whether to store user information
    \return account[str], password[str]
    """
    # user info file exists and not empty
    if path.exists(USER_INFO_CONF) and path.getsize(USER_INFO_CONF):
        with open(USER_INFO_CONF, 'rb') as f:
            ans = [_.decode().strip('\n') for _ in f]
            return ans[:2]
    else:
        with open(USER_INFO_CONF, 'wb') as f:
            account = input('请输入学号/帐号:\n')
            password = getpass.getpass('请输入密碼(无回显):\n')
            if store:
                f.write('\n'.join([account, password]).encode())
            return account, password


def connect_internet(wired=True):
    """
    connect to Internet from inner school net
    """
    if is_connected():
        print('Already connect to Internet!')
        return True
    # acqurie account and password
    account, psw = login()
    headers = {
        'Host': '172.18.3.3', 
        'Connection': 'kep-alive',
        'Content-Length': '67',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Origin': 'http://172.18.3.3',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://172.18.3.3/0.htm',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-TW,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en;q=0.6,ja;q=0.5'
    }
    url = 'http://172.18.3.3/0.htm'
    if wired:
        headers['Host'] = '172.18.2.2'
        headers['Origin'] = 'http://172.18.2.2'
        headers['Referer'] = 'http://172.18.2.2/0.htm'
        url = 'http://172.18.2.2/0.htm'
    data = {
        'DDDDD': account,
        'upass': psw,
        '0MKKey': '%B5%C7+%C2%BC%A1%A1Login',
        'v6ip': ''
    }
    # make POST request
    html = requests.post(url, headers=headers, data=data)
    res = BeautifulSoup(html.text, 'lxml')
    msg = res.title.string
    if msg == '登录成功':
        print('login successfully!')
        if is_connected():
            print('network OK!')
        else:
            print('network still has problems...')
            if wired:
                # try in another way
                return connect_internet(False)
        return True
    else:
        print('log in failed! Error message:\n', msg)
        # clear incorrect info
        with open(USER_INFO_CONF, 'w') as f:
            pass
        return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'wired':
            connect_internet(True)
        elif sys.argv[1] == 'wireless':
            connect_internet(False)
    else:
        connect_internet()
