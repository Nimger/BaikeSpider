# -*- codeing:UTF-8 -*-

from bs4 import BeautifulSoup as bs
import re

class HtmlParser(object):

	def parser_title(self,content):
		soup = bs(content,'html.parser')
		try:
			title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1').get_text()
		except:
			print('获取标题失败')
			return None
		else:
			return title

	def parser_summary(self,content):
		soup = bs(content,'html.parser')
		try:
			summary = soup.find('div',class_='lemma-summary').get_text()
		except:
			summary = soup.find('div',class_='para').get_text()
			return summary
		else:
			return summary


	def parser_urls(self,content):
		soup = bs(content,'html.parser')
		urls = soup.find_all('a',href=re.compile(r'/view/\d+\.htm'))
		url_list = []
		for url in urls:
			url_list.append('http://baike.baidu.com'+url['href'])

		return url_list


	def parser_title_urls(self):
		pass