# _*_ coding:utf-8 _*_

from otc_models import *

class otc_viewer(object):
	def __init__(self):
		pass

	def start(self):
		self.t = treading.Thread(target=self.__show_data,name = "ShowData")
		self.t.setDaemon(True)
		self.t.start()

	def __show_data(self):
		while(True):
			# Show Data
			time.sleep(0.2)
