import requests
from bs4 import BeautifulSoup
import pprint

url = "https://news.ycombinator.com/"
res = requests.get(url)
res2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body)

soup2 = BeautifulSoup(res2.text, 'html.parser')

title = soup.select('.storylink')
# score = soup.select('.score')
subtext = soup.select('.subtext')

title2 =soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_titles = title + title2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(list):
	#sorted by points from small to big number
	#https://towardsdatascience.com/sorting-a-dictionary-in-python-4280451e1637
	return sorted(list, key = lambda x:x['points'], reverse = True)

def create_custom(title, subtext):
	new_list = []
	for idx, item in enumerate(title):
		new_title = title[idx].getText()
		href = title[idx].get('href', None)
		
		new_score = subtext[idx].select('.score') #return a list
		if len(new_score) : ##if len() is not 0
			#new_score is a list, you should get the first element.
			points = int(new_score[0].getText().replace(" points",""))
			if points > 99:
				new_list.append({'title': new_title, 'link': href, 'points': points})
	return sort_stories_by_votes(new_list)

pprint.pprint(create_custom(mega_titles, mega_subtext))
