import requests
from bs4 import BeautifulSoup
from time import sleep  # нужно что бы сайт думал что действует человек
import xlsxwriter

# хэдерс делается чтобы сайт думла что действует человек
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)'}


def download(url):
    resp = requests.get(url,
                        stream=True)  # stream=True хначит что картинка будет грузится по мере загрузки минуя оперативку
    r = open(r'C:\Users\Paul\Desktop\images\\' + url.split('/')[-1], 'wb')
    for value in resp.iter_content(1048576):  # 1048576 = 1024 * 1024 или 1 мегабайт
        r.write(value)
    r.close()


def get_url():
    for count in range(1, 8):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')  # получаем все данные со страницы
        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')  # в диве нужный нам класс с таким названием
        for i in data:
            card_url = 'https://scrapingclub.com' + i.find('a').get('href')
            yield card_url  # в этот момент весь код в функции выше превращается в генератор


def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', class_='card mt-4 my-4')
        name = data.find('h3', class_='card-title').text
        price = data.find('h4').text
        text = data.find('p', class_='card-text').text
        url_img = 'https://scrapingclub.com' + data.find('img').get('src')  # , class_='card-img-top img-fluid'
        download(url_img)
        yield name, price, text, url_img


# создаем xlxs файл т.е. excel файл с help библиотеки xlsxwriter
def writer(parametr):
    book = xlsxwriter.Workbook(r'C:\Users\Paul\Desktop\data.xlsx')
    page = book.add_worksheet('товар')

    row = 0
    column = 0

    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 2, item[2])
        page.write(row, column + 3, item[3])
        row += 1
    book.close()


writer(array)
