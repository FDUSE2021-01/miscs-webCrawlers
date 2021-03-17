import lib
from bs4 import BeautifulSoup
import re
import pandas as pd

if __name__ == '__main__':
    URI = 'https://store.steampowered.com/search/?specials=1&page=1'
    text = lib.get_text(URI)
    if not text:
        quit()
    soup = BeautifulSoup(text, 'html.parser')
    print('page 1 grabbed')
    results = []
    for resultRow in soup.find_all(class_= 'search_result_row'):
        result = resultRow.attrs
        result['item_name'] = resultRow.find(class_='title').string
        # targeted platforms
        result['platform'] = []
        if (resultRow.select('.platform_img.win')):
            result['platform'].append('windows')
        if (resultRow.select('.platform_img.mac')):
            result['platform'].append('macos')
        if (resultRow.select('.platform_img.linux')):
            result['platform'].append('linux')
        result['release_date'] = resultRow.find(class_='search_released').string
        if (rating:=resultRow.find(class_='search_review_summary')):
            rating = rating['data-tooltip-html']
            reMatch = re.search(r'(\d+?%) of the (\S+?) user reviews', rating)
            try:
                result['rating_positive_ratio'], result['rating_count'] = \
                    reMatch.group(1, 2)
            except:
                pass
        prices = list(resultRow.find(class_='search_price').stripped_strings)
        if (len(prices) >= 2):
            result['original_pricing'] = prices[0]
        result['pricing'] = prices[-1]
        results.append(result)
    frame = pd.DataFrame.from_records(results)
    frame.to_excel('results/temp.xlsx')