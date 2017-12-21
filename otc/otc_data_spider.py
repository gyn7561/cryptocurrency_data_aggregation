# _*_ coding:utf-8 _*_

import time, threading
import requests

class otc_spider(object):
	def __init__(self,url,rate,data_callback):
		self.url = url
		self.rate = rate
		self.data_callback = data_callback

	def start(self):
		self.t = threading.Thread(target=self.__download_loop, name="LoopThread")
		self.t.setDaemon(True)
		self.t.start()

	def __download_loop(self):
		while(True):
			headers = {
        		#"Content-type": "application/x-www-form-urlencoded",
        		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    		}

			try:
				response = requests.get(self.url,None,headers=headers,timeout=5)
				if(response.status_code == 200):
					data = response.json()
					self.data_callback(data)
			except BaseException as e:
				print("Http Faild:",self.url)
				print(e)

			#print(self.url)
			#self.callback()
			time.sleep(self.rate)