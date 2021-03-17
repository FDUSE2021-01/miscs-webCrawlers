import requests
import pandas as pd
from bs4 import BeautifulSoup
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