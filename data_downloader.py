# coding: utf-8

import time, threading

class downloader(object):
	def __init__(self, url, rate, callback):
		self.url = url
		self.rate = rate
		self.callback = callback

	def start(self):
		self.t = threading.Thread(target=self.__download_looop,name="LoopThread")
		self.t.setDaemon(True)
		self.t.start()


	def __download_looop(self):
		while(True):
			print(self.url)
			self.callback()
			time.sleep(self.rate)

