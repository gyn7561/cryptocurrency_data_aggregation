# _*_ coding:utf-8 _*_

from otc_models import *
import threading
import sys, io, os, time

class otc_viewer(object):
	def __init__(self):
		pass

	def start(self):
		#self.t = threading.Thread(target=self.__show_data,name = "ShowData")
		#self.t.setDaemon(True)
		#self.t.start()
		self.__show_data()

	def __show_otc_huobi_buy_btc_trades(self):
		for item in otc_huobi_buy_btc_trades:
			str = "{0} {1}~{2} {3}".format(item.trader, item.min_amount, item.max_amount, item.price)
			print(str)
			#sys.stdout.write(str)
			#sys.stdout.flush()

	def __clear_screen(self):
		os.system('cls' if os.name=='nt' else 'clear')

	def __show_data(self):
		while(True):
			#self.__clear_screen()
			self.__show_otc_huobi_buy_btc_trades()
			time.sleep(1)