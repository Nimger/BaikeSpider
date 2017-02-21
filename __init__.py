# -*- coding=utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import re
from BaikeSpider import url_manager, html_downloader, html_parser, html_outputer


start_url = 'http://baike.baidu.com/link?url=ApeeWWd1n_liyZMLKDPkbpa8rzEX6vMRZJ31I4U8FT3XoFd1xZiZyLT7Orm_AMIZQ_sM3XTKGJws5mnhEujgeq'

class Spider(object):

	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.output = html_outputer.HtmlOutputer()

	def craw(self,root_url):
		index = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			print('craw %d' % index)

			url = self.urls.get_new_url()
			print('url = %s' % url)
			content = self.downloader.download(url)
			if content == None:
				continue
			title = self.parser.parser_title(content)
			if title == None:
				continue
			summary = self.parser.parser_summary(content)
			if summary == None:
				continue
			print('title %s summary %s' % (title,summary))
			urls = self.parser.parser_urls(content)
			self.urls.add_new_urls(urls)
			index += 1
			if index > 50:
				break

if __name__ == '__main__':
	spider = Spider()
	spider.craw(start_url)