#!/bin/python3

import lib
from bs4 import BeautifulSoup
import re
import pandas as pd
import argparse

def main(config: dict):
    itemName = lib.str2itadPlainName(config.itemName)
    URI = f'https://isthereanydeal.com/ajax/game/info?plain=halflifealyx{pageNumber}'
    text = lib.get_text(URI)
    if not text:
        print(URI, 'failed to load.')
        return
    frame = pd.read_html(text)
    if not frame:
        return
    frame = frame[0]
    lowestPrice = frame[frame['Store'] == 'Steam']['Lowest'].item()

def daily():
    raise NotImplementedError()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='get lowest price of item on steam')
    parser.add_argument('-i', '--item-name', dest='itemName',
                        help='the name of the item',
                        type=str)

    args = parser.parse_args()
    main(args)
    