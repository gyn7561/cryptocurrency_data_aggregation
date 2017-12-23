# _*_ coding:utf-8 _*_

#from otc_models import *
import threading
import otc_models
import sys, io, os, time

class otc_viewer(object):
	def __init__(self):
		pass

	def start(self):
		self.t = threading.Thread(target=self.__show_data,name = "ShowData")
		self.t.setDaemon(True)
		self.t.start()
		#self.__show_data()

	def __show_otc_huobi_buy_btc_trades(self):

		if(otc_models.otc_huobi_buy_btc_trades is None):
			sys.stdout.write("火币OTC买入BTC数据失败")
			sys.stdout.flush()
			return

		for item in otc_models.otc_huobi_buy_btc_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
		sys.stdout.write('----------------------------------------------------\n')
		sys.stdout.flush()

	def __show_otc_huobi_sell_btc_trades(self):
		if(otc_models.otc_huobi_sell_btc_trades is None):
			sys.stdout.write("火币OTC卖出BTC数据失败")
			sys.stdout.flush()
			return

		for item in otc_models.otc_huobi_sell_btc_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
		sys.stdout.write('----------------------------------------------------\n')
		sys.stdout.flush()

	def __show_otc_huobi_buy_usdt_trades(self):
		if(otc_models.otc_huobi_buy_usdt_trades is None):
			sys.stdout.write("火币OTC买入USDT数据失败")
			sys.stdout.flush()
			return

		for item in otc_models.otc_huobi_buy_usdt_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
		sys.stdout.write('----------------------------------------------------\n')
		sys.stdout.flush()

	def __show_otc_huobi_sell_usdt_trades(self):
		if(otc_models.otc_huobi_sell_usdt_trades is None):
			sys.stdout.write("火币OTC卖出USDT数据失败")
			sys.stdout.flush()
			return

		for item in otc_models.otc_huobi_sell_usdt_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
		sys.stdout.write('----------------------------------------------------\n')
		sys.stdout.flush()

	def __show_otc_coincola_buy_btc_trades(self):
		if(otc_models.otc_coincola_buy_btc_trades is None):
			sys.stdout.write("CoinCola买入BTC数据失败")
			sys.stdout.flush()
			return

		for item in otc_models.otc_coincola_buy_btc_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
		sys.stdout.write('----------------------------------------------------\n')
		sys.stdout.flush()

	def __show_otc_coincola_sell_btc_trades(self):
		if(otc_models.otc_coincola_sell_btc_trades is None):
			sys.stdout.write("CoinCola卖出BTC数据失败")
			sys.stdout.flush()
			return

		for item in otc_models.otc_coincola_sell_btc_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
		sys.stdout.write('----------------------------------------------------\n')
		sys.stdout.flush()

	def __show_otc_coincola_buy_eth_trades(self):
		if(otc_models.otc_coincola_buy_eth_trades is None):
			sys.stdout.write("CoinCola买入ETH数据失败")
			sys.stdout.flush()
			return

		for item in otc_models.otc_coincola_buy_eth_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
		sys.stdout.write('----------------------------------------------------\n')
		sys.stdout.flush()

	def __show_otc_coincola_sell_eth_trades(self):
		if(otc_models.otc_coincola_sell_eth_trades is None):
			sys.stdout.write("CoinCola卖出ETH数据失败")
			sys.stdout.flush()
			return

		for item in otc_models.otc_coincola_sell_eth_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
		sys.stdout.write('----------------------------------------------------\n')
		sys.stdout.flush()

	def __show_otc_coincola_buy_bch_trades(self):
		if(otc_models.otc_coincola_buy_bch_trades is None):
			sys.stdout.write("CoinCola买入BCH数据失败")
			sys.stdout.flush()
			return

		for item in otc_models.otc_coincola_buy_bch_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
		sys.stdout.write('----------------------------------------------------\n')
		sys.stdout.flush()


	def __show_otc_coincola_sell_bch_trades(self):
		if(otc_models.otc_coincola_sell_bch_trades is None):
			sys.stdout.write("CoinCola卖出BCH数据失败")
			sys.stdout.flush()
			return

		for item in otc_models.otc_coincola_sell_bch_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
		sys.stdout.write('----------------------------------------------------\n')
		sys.stdout.flush()

	def __show_otc_okex_buy_btc_trades(self):
		for item in otc_models.otc_okex_buy_btc_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
		sys.stdout.write('----------------------------------------------------\n')
		sys.stdout.flush()

	def __show_otc_okex_sell_btc_trades(self):
		for item in otc_models.otc_okex_sell_btc_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
		sys.stdout.write('----------------------------------------------------\n')
		sys.stdout.flush()

	def __show_otc_okex_buy_eth_trades(self):
		for item in otc_models.otc_okex_buy_eth_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
		sys.stdout.write('----------------------------------------------------\n')
		sys.stdout.flush()

	def __show_otc_okex_sell_eth_trades(self):
		for item in otc_models.otc_okex_sell_eth_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
		sys.stdout.write('----------------------------------------------------\n')
		sys.stdout.flush()

	def __clear_screen(self):
		os.system('cls' if os.name=='nt' else 'clear')

	def __show_data(self):
		while(True):
			self.__clear_screen()
			self.__show_otc_huobi_buy_btc_trades()
			self.__show_otc_huobi_sell_btc_trades()
			self.__show_otc_huobi_buy_usdt_trades()
			self.__show_otc_huobi_sell_usdt_trades()
			self.__show_otc_coincola_buy_btc_trades()
			self.__show_otc_coincola_sell_btc_trades()
			self.__show_otc_coincola_buy_eth_trades()
			self.__show_otc_coincola_sell_eth_trades()
			self.__show_otc_coincola_buy_bch_trades()
			self.__show_otc_coincola_sell_bch_trades()

			time.sleep(1)