from bs4 import BeautifulSoup
import requests
class find_site_with_news_of_category(object):
	def __init__(self):
		#ссылка на сайт
		#url = {
		#	1 : "https://ria.ru/",
		#	2 : "https://tass.ru/",
		#	3 : "https://www.interfax.ru/",
		#	4 : "https://www.rbc.ru/",
		#	5 : "https://lenta.ru/",
		#	6 : "https://www.vedomosti.ru/",
		#	7 : "https://www.gazeta.ru/",
		#	8 : "https://www.kommersant.ru/",
		#	9 : "https://www.vesti.ru/",
		#	10 : "https://echo.msk.ru/",
		#	11 : "https://svpressa.ru/",
		#	12 : "https://tvrain.ru/",
		#	13 : "https://rg.ru/",
		#	14 : "https://life.ru/"
		#}
		##идентификация кода в виде пользователя
		#headers = {
		#	"Accept" : "*/*",
		#	"User-Agent" : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.234 Yowser/2.5 Safari/537.36"
		#}
		##переход на сайт с помощью кода
		#for i in range(1,15):
		#	req = requests.get(url[i], headers=headers)
		#	src = req.text
		##print(src)
		#	with open(("url"+str(i)+".html"), "w", encoding="UTF-8") as file:
		#		file.write(src)

		#прописаны классы соответственно новостному сайту
		cls_ = {
			1 : "footer__rubric-item",
			2 : "menu-sections-list__title-wrapper",
			3 : "toplinks",
			4 : "https://www.rbc.ru/",
			5 : "https://lenta.ru/",
			6 : "https://www.vedomosti.ru/",
			7 : "https://www.gazeta.ru/",
			8 : "https://www.kommersant.ru/",
			9 : "https://www.vesti.ru/",
			10 : "https://echo.msk.ru/",
			11 : "https://svpressa.ru/",
			12 : "https://tvrain.ru/",
			13 : "https://rg.ru/",
			14 : "https://life.ru/"
		}
		for i in range(1,4):
			#чтение файлов через цикл
			with open("url"+str(i)+".html", "r", encoding="UTF-8") as file:
				src = file.read()
			soup = BeautifulSoup(src, "lxml")
			#ищет класс
			all_category_of_news = soup.find_all(class_=cls_[i])
			#исключение: ищет класс и тег а, ибо там содержится инфа
			if i == 3:
				all_category_of_news = soup.find(class_=cls_[i]).find_all("a")
			#прописывает в консоль
			for item in all_category_of_news:
				item_text = item.text
				if i ==3:
					item_href = item.get("href")
				else:
					item_href = item.find("a", href=True).get("href")
				print(f"{item_text} : {item_href}")
find_site_with_news_of_category()