import requests
from bs4 import BeautifulSoup as Bs
import json

url_main = 'https://www.work.ua/ru/jobs-odesa/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    }

page_main = requests.get(url_main, headers=headers)
with open('test.html', 'wb') as of:
    of.write(page_main.text.encode('utf-8'))
soup_main = Bs(page_main.text, "html.parser")
page_list = soup_main.find_all('li', class_='')

jobs = {}

for page_number in int(page_list[3].a.text):
    url_page = 'https://www.work.ua/ru/jobs-odesa/?page=%d' % page_number
    page_active = requests.get(url_page, headers=headers)
    soup_page = Bs(page_active.text, "html.parser")
    vacancies_names = soup_page.find_all('div', class_='card card-hover card-visited wordwrap job-link js-hot-block')
    vacancies_info = soup_page.find_all('p', class_='overflow text-muted add-top-sm add-bottom')
    company_list = soup_page.find_all('div', class_='add-top-xs')
    for vacancy_number in vacancies_names.items():
        jobs[company_list.span.b.text] = (vacancies_names.h2.a['title'], 'https://www.work.ua'+vacancies_names.h2.a['href'], vacancies_info.text)
with open('test.json', 'wb', encoding='utf-8') as doc:
    stuff = json.dumps(jobs, ensure_ascii=False)
    doc.write(stuff)
