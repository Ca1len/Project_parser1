import requests
from bs4 import BeautifulSoup as Bs
import json

URL_TEMPLATE = "https://www.work.ua/ru/jobs-odesa/?page=2"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'cookie': 'plastikovye-vospominaniya=1477.11; _ga=GA1.2.324220759.1581889231; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6ImFadlVRWnY3aTBtTFhyUFI3ZmtoMEE9PSIsInZhbHVlIjoiNzhSK0R2eGdOMVBJTE5BWTBlOEt4ZUJIRmEyN2ZTQzdYODVhN3pGZUVnbm5OaStaSDVMK2V0Y0trOGlpUGRwaXVDb0FPb1wvRHNiZmxITXpFQituY0VKXC9ySXM1M3o2YmFTYTRRV2c5VzZaSEltZW1DZUFXQ252bDdwSFU1R2NFWStmYzgzaXpoVmw4M3dLVTc5RXljS2JDWWJuMXZ6VkRqYTNWdWprZFBYNVN0Zm9BYkdvRFwvUk5LUEsybU5zdW9nIiwibWFjIjoiNzE2N2YzYjBmNTc1YWUzZjA0ZWM5ZjIxMGExNzk2MTJlMjM3ODY2MGE5ZDNhMDY5ODFmZWJhNzdlMzlkZWRmYyJ9; __atssc=vk%3B5; _gid=GA1.2.999237229.1593986215; cf_chl_1=f785ed8de6ea7ef; __atuvc=48%7C25%2C45%7C26%2C9%7C27%2C32%7C28%2C6%7C29; XSRF-TOKEN=eyJpdiI6IlwvcGRWTnJJbzEzeFh5T0Y4WE01UkR3PT0iLCJ2YWx1ZSI6IlM3MWxQVElWOWt5QjM4ZGVjVFJhNDNZeENXeDJVZDd0cWpPbld3YjkwR0g2WlJqNnorQ1NaZ1lENngxWkdqT1oiLCJtYWMiOiJhMGI2NGIzMDExYWNjMDA3MTNmODhhZTIzNTcxZjU3ZWIzZjBiNjhmY2YyNjA0MTcwZjYxYzZjOTdmNmQ1ZGJmIn0%3D; laravel_session=eyJpdiI6ImhIbkVMZ2U4aTJNaVZwcnhkZHVqK1E9PSIsInZhbHVlIjoibTNNVlpnSFo3T0RJMTRnbGQrN2t3U2JVeFZ3bHVYUVdDNTVSYXZVa2FPSjRqVldJTUdjYThYQ0dhclBQWE1oSyIsIm1hYyI6ImVkMTc3NzkwMDk3NGRlYWQ1NjMwYWVjNjc1ODAzMjI2MzE2NmU1MTliOTkxMDdmNDA3ZjU4Zjc5MGMxYjI5MjIifQ%3D%3D'
    }

r = requests.get(URL_TEMPLATE, headers=headers)
with open('test.html', 'wb') as output_file:
    output_file.write(r.text.encode('utf-8'))
soup = Bs(r.text, "html.parser")
vacancies_names = soup.find_all('div', class_='card card-hover card-visited wordwrap job-link js-hot-block')
vacancies_info = soup.find_all('p', class_='overflow text-muted add-top-sm add-bottom')
_vacancies = zip(vacancies_names, vacancies_info)
vacancies = {vacancies_[0]: vacancies_[1] for vacancies_ in _vacancies}
for info in vacancies.items():
    print('+++'*10)
    print(info[0].h2.a['title'])
    print('https://www.work.ua'+info[0].a['href'])
    print(info[1].text)
    print('+++'*10)
_vacancies = zip(vacancies_names, vacancies_info)
vacancies = {str(vacancies_[0].h2.a['title']): vacancies_[1].text for vacancies_ in _vacancies}
print(vacancies)
with open('test.json', 'w', encoding="utf-8") as doc:
    info = json.dumps(vacancies, ensure_ascii=False)
    doc.write(info)

# {
#    название_компании: {"должность": должность, "описание": описание}
# }
