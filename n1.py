import time
from typing import Dict, List

import requests
from bs4 import BeautifulSoup as Bs
import json

URL_MAIN = 'https://www.work.ua/ru/jobs-odesa/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    }

def count_of_pages() -> int:
    page_main = requests.get(URL_MAIN, headers=HEADERS)
    with open('test.html', 'wb') as of:
        of.write(page_main.text.encode('utf-8'))
    soup_main = Bs(page_main.text, "html.parser")
    page_list = soup_main.find_all('ul', class_="pagination hidden-xs")
    return int(str(page_list[0]).split('</li>')[-3].split('>')[-2].split('</a')[0])


def clear_json():
    with open('test.json', 'w', encoding='utf-8') as dick:
        dick.write('')


def main():
    url_page = 'https://www.work.ua/ru/jobs-odesa/?page={}'
    with open('test.json', 'a', encoding='utf-8') as doc:
        for page_number in range(count_of_pages()):
            result = parse_page(page_number, url_page)
            if not result:
                print('GG WP ', page_number)
            else:
                stuff = json.dumps(result, ensure_ascii=False)
                doc.write(stuff)
    #TODO: Подключить это говно к БД
    #TODO: Научиться парсить дальше 7 страницы
def parse_page(page_number: int, url_pattern: str) -> Dict[str, List[str]]:
    jobs = {}
    page_active = requests.get(url_pattern.format(page_number), headers=HEADERS)
    soup_page = Bs(page_active.text, "html.parser")
    vacancies_names = soup_page.find_all('div', class_='card card-hover card-visited wordwrap job-link js-hot-block')
    for vacancy in vacancies_names:
        company = vacancy.find('div', class_='add-top-xs').span.b.text
        jobs[company] = (
            vacancy.h2.a['title'], 'https://www.work.ua' + vacancy.h2.a['href'], vacancy.p.text)
    return jobs


if __name__ == '__main__':
    clear_json()
    main()
