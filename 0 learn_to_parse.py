# import requests
# from bs4 import BeautifulSoup
#
#
# url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
#
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, 'lxml')
#
# data = soup.find('div', class_='col-lg-4 col-md-6 mb-4')  # в диве нужный нам класс с таким названием
#
# name = data.find('h4', class_='card-title').text.replace('\n', '')  # метод text и не надо самому сплитить название, replace для удаления красных строк
# price = data.find('h5').text
# url_img = data.find('a')
# print(url_img)


s = '<a href="/exercise/list_basic_detail/90008-E/"><img alt="" class="card-img-top img-fluid" src="/static/img/90008-E.jpg"/></a>'

s = s.split('src=')
print(s[1][:-6])


# 16-35