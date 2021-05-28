from bs4 import BeautifulSoup
import requests
#ссылка на сайт
url = {
	1 : "https://ria.ru/",
	2 : "https://tass.ru/",
	3 : "https://www.interfax.ru/",
	4 : "https://www.rbc.ru/",
	5 : "https://lenta.ru/",
	6 : "https://www.gazeta.ru/",
	7 : "https://www.kommersant.ru/",
	8 : "https://smotrim.ru/articles",
	9 : "https://echo.msk.ru/",
	10 : "https://svpressa.ru/",
	11 : "https://tvrain.ru/",
	12 : "https://rg.ru/",
}
class find_site_with_news_of_category(object):
	def __init__(self):
		global url
		#прописаны классы соответственно новостному сайту
		cls_ = {
			1 : "cell-list__item m-no-image",
			2 : "popular-news__item",
			3 : "newsmain",
			4 : "js-news-feed-list",
			5 : "b-yellow-box__wrap",
			6 : "sausage-list-item news_title",
			7 : "place-newsline",
			8 : "news__content",
			9 : "newspreview",
			10 : "b-news__title",
			11 : "mainNews",
			12 : "b-feed__list_com",
		}
		for i in range(1,13):
			print(f"\n{url[i]}\n")
			#чтение файлов через цикл
			with open("url"+str(i)+".html", "r", encoding="UTF-8") as file:
				src = file.read()
			soup = BeautifulSoup(src, "lxml")
			#ищет класс
			all_category_of_news = soup.find_all(class_=cls_[i])
			#исключение: ищет класс и тег а, ибо там содержится инфа
			if i == 3 or i == 4 or i == 5 or i == 11 or i == 12:
				all_category_of_news = soup.find(class_=cls_[i]).find_all("a")
			elif i == 7 or i == 8 or i == 9:
				all_category_of_news = soup.find(class_=cls_[i]).find_all("h3")
			#print(len(all_category_of_news))
			#print(all_category_of_news)
			#считает количество новостей
			val = 0
			for m in all_category_of_news:
				val+=1
			print(f"Количество новостей {val}")
			#прописывает в консоль
			for item in all_category_of_news:
				if i == 4:
					item_text = item.find("span").text
				elif i == 6:
					item_text = item.find("span", itemprop="headline").text
				else:
					item_text = item.text
				if i == 3 or i == 4 or i == 5 or i == 10 or i == 11 or i == 12:
					item_href = item.get("href")
				else:
					item_href = item.find("a", href=True).get("href")
				print(f"{item_text} : {item_href}")
def loading():
	global url
	#идентификация кода в виде пользователя
	headers = {
		"Accept" : "*/*",
		"User-Agent" : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.234 Yowser/2.5 Safari/537.36"
	}
	#переход на сайт с помощью кода
	for i in range(1,13):
		req = requests.get(url[i], headers=headers)
		src = req.text
	#print(src)
		with open(("url"+str(i)+".html"), "w", encoding="UTF-8") as file:
			file.write(src)
loading()
find_site_with_news_of_category()