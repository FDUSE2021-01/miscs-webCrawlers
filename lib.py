import requests
import pandas as pd
from bs4 import BeautifulSoup
import re 

def get_text(url):
    try:
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/85.0.4183.102 Safari/537.36' # , 'Accept-Language': 'zh-CN '
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def str2itadPlainName(appName: str) -> str:
    appName = appName.lower()
    appName = re.sub(r'[^a-z\d', '', appName)
    covDict = {
        '0': '0',
        '1': 'i',
        '2': 'ii',
        '3': 'iii',
        '4': 'iv',
        '5': 'v',
        '6': 'vi',
        '7': 'vii',
        '8': 'viii',
        '9': 'ix',
    }
    return re.sub(r'\d', lambda x:covDict[x.group(0)], appName)