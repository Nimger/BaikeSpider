# -*- codeing:UTF-8 -*-

import requests

class HtmlDownloader(object):

	def __init__(self):
		self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

	def download(self,url):
		resp = requests.get(url,headers=self.headers)
		resp.encoding = 'UTF-8'
		print('status code:[%d]' % resp.status_code)
		if resp.status_code == requests.codes.ok:
			return resp.text
		else:
			return None

