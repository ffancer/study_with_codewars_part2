from requests import Session  # для сохранения файлов куки
from bs4 import BeautifulSoup


# хэдерс делается чтобы сайт думла что действует человек
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 '
                  '(.NET CLR 3.5.30729)'}

# имитация того, что на сайт заходит человек
work = Session()
work.get('https://quotes.toscrape.com/', headers=headers)
response = work.get('https://quotes.toscrape.com/login', headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
print(soup)