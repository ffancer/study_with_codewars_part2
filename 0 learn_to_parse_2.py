from requests import Session  # для сохранения файлов куки
from bs4 import BeautifulSoup
import xlsxwriter


# хэдерс делается чтобы сайт думла что действует человек
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 '
                  '(.NET CLR 3.5.30729)'}

# имитация того, что на сайт заходит человек
work = Session()
work.get('https://quotes.toscrape.com/', headers=headers)
response = work.get('https://quotes.toscrape.com/login', headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
token = soup.find('form').find('input').get('value')
data = {'csrf_token': token,
        'username': 'noname',
        'password': 'password'
        }

# наш запрос проходит 3 стадии, это и будет отображено далее
# по умолчанию перенаправление не поддерживается но allow_redirects=True разрешает
result = work.post('https://quotes.toscrape.com/login', headers=headers, data=data, allow_redirects=True)
# print(result.text)

soup2 = BeautifulSoup(result.text, 'lxml')


def array():

    quote = soup2.find('div', class_='quote').find('span', class_='text').text
    author = soup2.find('small', class_='author').text
    # tags = soup2.find('div', class_='tags').text.split(':')[1]
    tags = soup2.find('div', class_='tags').find('meta', class_="keywords").get('content')
    yield quote, author, tags
    # return tags

# print(array())
def writer(parametr):
    book = xlsxwriter.Workbook(r'C:\Users\Paul\Desktop\quoters.xlsx')
    page = book.add_worksheet('цитаты и авторы с тегами')

    row = 0
    column = 0

    page.set_column("A:A", 100)
    page.set_column("B:B", 15)
    page.set_column("C:C", 40)


    for item in parametr:
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 2, item[2])
        row += 1
    book.close()


writer(array())


