import requests as rq
from bs4 import BeautifulSoup
import wget

def main():
	name = input('enter anime name: ')
	URL = f"https://gogoanime.ai//search.html?keyword={name}"

	html = rq.get(URL)

	if(html.status_code != 200):
		print('sorry! something is wrong please report to this url: ')
		return

	soup = BeautifulSoup(html.text, 'html.parser')

	names = soup.find_all(class_='name')
	if(len(names) <= 0):
		print('no result found')
		return

	index = 1
	all_anime_name = {}
	
	for i in names:
		print(index ,i.get_text())
		all_anime_name[index] = i.get_text()
		index = index + 1

	select_anime_name = int(input('choose anime: '))
	anime_name = all_anime_name.get(select_anime_name)
	if(anime_name):
		anime_download(anime_name)
	else:
		print('wrong choice')

def anime_download(anime_name):
	input_from = int(input('from: '))
	input_to = int(input('to: '))

	anime_name = anime_name.replace(" ", '-')
	for i in range(input_from, input_to + 1):
		URL = f"https://gogoanime.ai/{anime_name}-episode-{i}"

		html = rq.get(URL)
		soup = BeautifulSoup(html.text, 'html.parser')
		
		download_btn = soup.find(class_='dowloads')
		download_site = str(download_btn.find('a')['href'])

		
		html2 = rq.get(download_site)
		soup2 = BeautifulSoup(html2.text, 'html.parser')

		download_list = soup2.find(class_='mirror_link')
		download_btn_2 = download_list.find_all(class_='dowload')[-1]

		download_link = str(download_btn_2.find('a')['href'])
		filename = wget.download(download_link)
		print(filename, 'completed')


if(__name__ == '__main__'):
	main()