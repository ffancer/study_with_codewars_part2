import requests
from bs4 import BeautifulSoup


url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

response = requests.get(url)

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
    name = i.find('h4', class_='card-title').text.replace('\n', '')
    price = i.find('h5').text
    url_img = 'https://scrapingclub.com' + i.find('img', class_='card-img-top img-fluid').get('src')
    print(name, price, url_img, sep='\n')

#



