from bs4 import BeautifulSoup
import requests
class find_site_with_news(object):
	def __init__(self, theme):
		pass
#ссылка на сайт
url1 = "https://ria.ru/"
#идентификация кода в виде пользователя
headers = {
	"Accept" : "*/*",
	"User-Agent" : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.234 Yowser/2.5 Safari/537.36"
}
#переход на сайт с помощью кода
req = requests.get(url1, headers=headers)
src = req.text
#print(src)