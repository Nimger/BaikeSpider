# -*- codeing:UTF-8 -*-

class UrlManager:

	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()

	def add_new_url(self,url):
		if url not in self.old_urls and url not in self.new_urls:
			self.new_urls.add(url)

	def add_new_urls(self,urls):
		for url in urls:
			self.add_new_url(url)

	def has_new_url(self):
		return len(self.new_urls)

	def get_new_url(self):
		return self.new_urls.pop()

