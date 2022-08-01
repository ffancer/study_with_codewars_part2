import requests
from bs4 import BeautifulSoup
from time import sleep  # нужно что бы сайт думал что действует человек

lst_card_url = []
# хэдерс делается чтобы сайт думла что действует человек
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)'}

for count in range(1, 8):
    sleep(1)
    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')  # получаем все данные со страницы

    data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')  # в диве нужный нам класс с таким названием

    # для одной карточки:
    # name = data.find('h4', class_='card-title').text.replace('\n', '')  # метод text и не надо самому сплитить название, replace для удаления красных строк
    # price = data.find('h5').text
    #
    #     # url_img = data.find('a') #  мой способ
    #     # s = '<a href="/exercise/list_basic_detail/90008-E/"><img alt="" class="card-img-top img-fluid" src="/static/img/90008-E.jpg"/></a>'
    #     # s = s.split('src=')
    #     # print(s[1][:-6])
    # url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src')  # так мы достали картинку, намного легче моего способа выше


    # для всех фото-карточек с сайта метод find_all и меняем data на i (в отличие с одиночной краточкой)
    for i in data:
        # это удаляется
        # name = i.find('h4', class_='card-title').text.replace('\n', '')
        # price = i.find('h5').text
        # url_img = 'https://scrapingclub.com' + i.find('img', class_='card-img-top img-fluid').get('src')
        # print(name, price, url_img, sep='\n', end='\n\n')
        ###########################################################################################################
        card_url = 'https://scrapingclub.com' + i.find('a').get('href')
        lst_card_url.append(card_url)

for card_url in lst_card_url:
    response = requests.get(card_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='card mt-4 my-4')
    name = data.find('h3', class_='card-title').text
    price = data.find('h4').text
    text = data.find('p', class_='card-text').text
    url_img = 'https://scrapingclub.com' + data.find('img').get('src') # , class_='card-img-top img-fluid'
    print(name, price, text, url_img, sep='\n', end='\n\n')

# 47-23


