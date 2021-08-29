import requests, csv
from bs4 import BeautifulSoup
import pprint ##print更好看
##https://docs.python.org/3/library/pprint.html

url = 'https://movie.douban.com/top250'
# url = 'https://news.ycombinator.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
res = requests.get(url, headers = headers) 

# print(res) ## 200
# print(res.text) ##返回html文档

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
# print(soup.body)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# print(soup.find('a')) ##find the first a tag

# print(soup.select('.title')) ##css selector to select id=home
# print(soup.select('.rating_num')) ##css selector to select id=home

#1. find the title
movieList=soup.find('ol',attrs={'class':'grid_view'})
all_title = []
for MovieLi in movieList.find_all('li'):
    container_title = MovieLi.find('div',attrs={'class':'hd'})
    title = container_title.find('span', attrs={'class':'title'}).getText() ##找到第一个class=tile的
    all_title.append(title)
# print(all_title)

#2. find the rating
rating = soup.select('.rating_num')
print(rating)

#---------------form a csv------------------------
def write_to_csv():
    global rating, all_title
    with open('douban.csv', mode = 'a') as database:
        for idx, item in enumerate(all_title):
            title = all_title[idx]
            rates = rating[idx].getText()
            csv_writer = csv.writer(database, lineterminator='\n', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([title, rates])

write_to_csv()


# -----------------form a dict---------------------
def create_custom(all_title, rating):
    new_list = []
    #enumerate 列举 https://www.programiz.com/python-programming/methods/built-in/enumerate
    for idx, item in enumerate(all_title):
        name = all_title[idx] ## get the title
        # print(name)
        rates = float(rating[idx].getText())
        # print(rates)
        # print(rates)
        # # href = title[idx].get('href', None) ## get the href
        new_list.append({'电影': name, '评分': rates})
    return new_list

pprint.pprint(create_custom(all_title, rating))