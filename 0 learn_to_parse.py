# import requests
# from bs4 import BeautifulSoup
# import lxml
#
# url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
#
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, 'lxml')
#
# data = soup.find('div', class_='col-lg-4 col-md-6 mb-4')  # в диве нужный нам класс с таким названием
#
# name = data.find('h4', class_='card-title')
# print(name)

# s = '<a href="/exercise/list_basic_detail/90008-E/">Short Dress</a>'
s = '<a href="/exercise/list_basic_detail/90008-E/">Patterned Slacks</a>'

s = s.split('>')[1][:-3]
print(s)


# 16-35