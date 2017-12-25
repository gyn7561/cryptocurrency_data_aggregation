# _*_ coding:utf-8 _*_

#from otc_models import *
import threading
import otc_models
import sys, io, os, time

'''
def make_str_with_len(raw_str, length):
	real_len = len(raw_str.encode('utf-8'))
	space_count = 0
	if(real_len > length):
		sum = 0
		new_str = ""
		for char in raw_str:
			char_len = len(char.encode('utf-8'))
			sum = sum + char_len
			if (sum <= length):
				new_str = new_str + char
		return new_str, sum
	else:
		return raw_str, real_len
'''

def make_str_with_width(raw_str, width):
	real_len = 0
	new_str = ""
	for s in raw_str:
		if ord(s) > 127:
			s_width = 2
		else:
			s_width = 1
		if real_len + s_width <= width:
			real_len = real_len + s_width
			new_str = new_str + s
	#print(new_str,real_len)
	return new_str,real_len

def left_str_format(raw_str, width):
	new_str,real_len = make_str_with_width(raw_str, width)
	append_space = width - real_len
	real_width = len(raw_str) + append_space
	return ('{:<%d}' % real_width).format(new_str)

def right_str_format(raw_str, width):
	new_str,real_len = make_str_with_width(raw_str, width)
	append_space = width - real_len
	real_width = len(raw_str) + append_space
	#print("P:",new_str,real_len,append_space,real_width)
	return ('{:>%d}' % real_width).format(new_str)

def center_str_format(raw_str, width):
	new_str,real_len = make_str_with_width(raw_str, width)
	append_space = width - real_len
	real_width = len(raw_str) + append_space
	return ('{:^%d}' % real_width).format(new_str)




class otc_viewer(object):
	def __init__(self):
		pass

	def start(self):
		#self.t = threading.Thread(target=self.__show_data,name = "ShowData")
		#self.t.setDaemon(True)
		#self.t.start()
		self.__show_data()

	def __construct_trade_str(self,item):
		if(item is None):
			return ""

		trader = left_str_format(item.trader,10)
		min_amount = item.min_amount
		max_amount = item.max_amount
		amount_str = "{0}~{1}".format(int(min_amount),int(max_amount))
		amount_str = center_str_format(amount_str,20)
		price = int(item.price)
		output = "{0} {1} {2}".format(trader,amount_str,price)
		return output

	def __get_item_from_list(self,itemlist,index):
		if itemlist is None:
			return None
		if index >= len(itemlist):
			return None

		return itemlist[index]


	def __construct_out_str(self):
		for x in range(10):
			huobi_buy_btc_item = self.__get_item_from_list(otc_models.otc_huobi_buy_btc_trades,x)
			huobi_sell_btc_item = self.__get_item_from_list(otc_models.otc_huobi_sell_btc_trades,x)

			huobi_buy_btc_item_str = self.__construct_trade_str(huobi_buy_btc_item)
			huobi_sell_btc_item_str = self.__construct_trade_str(huobi_sell_btc_item)

			out_str = "{0}     {1}".format(huobi_buy_btc_item_str, huobi_sell_btc_item_str)

			print(out_str)


	def __show_otc_huobi_buy_btc_trades(self):

		if(otc_models.otc_huobi_buy_btc_trades is None):
			sys.stdout.write("火币OTC买入BTC数据失败")
			sys.stdout.flush()
			return

		for x in range(len(otc_models.otc_huobi_buy_btc_trades)):
			item = otc_models.otc_huobi_buy_btc_trades[x]

			trader = left_str_format(item.trader,15)
			min_amount = item.min_amount
			max_amount = item.max_amount
			amount_str = "{0}~{1}".format(int(min_amount),int(max_amount))
			amount_str = center_str_format(amount_str,20)
			price = int(item.price)
			output = "{0} {1} {2}".format(trader,amount_str,price)

			sys.stdout.write(output + "\n")
			sys.stdout.flush()

		'''
		for item in otc_models.otc_huobi_buy_btc_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
		'''
		#sys.stdout.write('----------------------------------------------------\n')
		#sys.stdout.flush()

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
			self.__construct_out_str()
			#self.__show_otc_huobi_buy_btc_trades()
			'''
			self.__show_otc_huobi_sell_btc_trades()
			self.__show_otc_huobi_buy_usdt_trades()
			self.__show_otc_huobi_sell_usdt_trades()
			self.__show_otc_coincola_buy_btc_trades()
			self.__show_otc_coincola_sell_btc_trades()
			self.__show_otc_coincola_buy_eth_trades()
			self.__show_otc_coincola_sell_eth_trades()
			self.__show_otc_coincola_buy_bch_trades()
			self.__show_otc_coincola_sell_bch_trades()
			'''

			time.sleep(2)