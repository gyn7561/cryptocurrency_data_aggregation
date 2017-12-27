# _*_ coding:utf-8 _*_

#from otc_models import *
'''
import threading
import otc_models
import sys, io, os, time


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






import otc_models
import threading
import sys, io, os, time
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from otc_main import *

class otc_viewer(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

		self.t = threading.Thread(target=self.updateUI, name="ViewerUpdate")
		self.t.setDaemon(True)
		self.t.start()

	def initUI(self):
		self.huobi_buy_btc_label = QLabel('Huobi Buy BTC Data')
		self.__set_label_style(self.huobi_buy_btc_label)
		self.huobi_sell_btc_label = QLabel('Huobi Sell BTC Data')
		self.__set_label_style(self.huobi_sell_btc_label)
		self.huobi_buy_usdt_label = QLabel('Huobi Buy USDT Data')
		self.__set_label_style(self.huobi_buy_usdt_label)
		self.huobi_sell_usdt_label = QLabel('Huobi Sell USDT Data')
		self.__set_label_style(self.huobi_sell_usdt_label)
		self.coincola_buy_btc_label = QLabel('CoinCola Buy BTC Data')
		self.__set_label_style(self.coincola_buy_btc_label)
		self.coincola_sell_btc_label = QLabel('CoinCola Sell BTC Data')
		self.__set_label_style(self.coincola_sell_btc_label)
		self.coincola_buy_eth_label = QLabel('CoinCola Buy ETH Data')
		self.__set_label_style(self.coincola_buy_eth_label)
		self.coincola_sell_eth_label = QLabel('CoinCola Sell ETH Data')
		self.__set_label_style(self.coincola_sell_eth_label)
		self.coincola_buy_bch_label = QLabel('CoinCola Buy BCH Data')
		self.__set_label_style(self.coincola_buy_bch_label)
		self.coincola_sell_bch_label = QLabel('CoinCola Sell BCH Data')
		self.__set_label_style(self.coincola_sell_bch_label)
		
		grid = QGridLayout()
		grid.setSpacing(30)
		

		grid.addWidget(self.huobi_buy_btc_label,1,0)
		grid.addWidget(self.huobi_sell_btc_label,1,1)
		grid.addWidget(self.huobi_buy_usdt_label,1,2)
		grid.addWidget(self.huobi_sell_usdt_label,1,3)
		grid.addWidget(self.coincola_buy_btc_label,2,0)
		grid.addWidget(self.coincola_sell_btc_label,2,1)
		grid.addWidget(self.coincola_buy_eth_label,2,2)
		grid.addWidget(self.coincola_sell_eth_label,2,3)
		grid.addWidget(self.coincola_buy_bch_label,3,0)
		grid.addWidget(self.coincola_sell_bch_label,3,1)

		self.setLayout(grid)

		self.resize(1920,1080)
		#self.setGeometry(0,0,1920,1080)
		self.setWindowTitle('OTC Data Viewer')
		self.show()


	def __set_label_style(self,label):
		label.setAlignment(Qt.AlignTop)
		label.setFont(QFont('SansSerif', 12)) 


	def __construct_trade_str(self,item):
		if(item is None):
			return ""

		trader = left_str_format(item.trader,10)
		min_amount = item.min_amount
		max_amount = item.max_amount
		amount_str = "{0} - {1}".format(int(min_amount),int(max_amount))
		amount_str = center_str_format(amount_str,20)
		price = item.price
		output = "{0} {1} {2}".format(trader,amount_str,price)
		return output

	def __construct_trade_list_str(self,trade_list):
		if trade_list is None:
			return None

		show_str = ""
		for trade in trade_list:
			show_str += self.__construct_trade_str(trade)
			show_str += "\n"
		return show_str

	def __show_otc_huobi_buy_btc_trades(self):
		show_str = self.__construct_trade_list_str(otc_models.otc_huobi_buy_btc_trades)
		if show_str is None:
			show_str = "Huobi Buy BTC Data Faild"
		else:
			show_str = "Huobi Buy BTC Data:\n" + show_str
		self.huobi_buy_btc_label.setText(show_str)

	def __show_otc_huobi_sell_btc_trades(self):
		show_str = self.__construct_trade_list_str(otc_models.otc_huobi_sell_btc_trades)
		if show_str is None:
			show_str = "Huobi Sell BTC Data Faild"
		else:
			show_str = "Huobi Sell BTC Data:\n" + show_str
		self.huobi_sell_btc_label.setText(show_str)

	def __show_otc_huobi_buy_usdt_trades(self):
		show_str = self.__construct_trade_list_str(otc_models.otc_huobi_buy_usdt_trades)
		if show_str is None:
			show_str = "Huobi Buy USDT Data Faild"
		else:
			show_str = "Huobi Buy USDT Data:\n" + show_str
		self.huobi_buy_usdt_label.setText(show_str)

	def __show_otc_huobi_sell_usdt_trades(self):
		show_str = self.__construct_trade_list_str(otc_models.otc_huobi_sell_usdt_trades)
		if show_str is None:
			show_str = "Houbi Sell USDT Data Faild"
		else:
			show_str = "Huobi Sell USDT Data:\n" + show_str
		self.huobi_sell_usdt_label.setText(show_str)

	def __show_otc_coincola_buy_btc_trades(self):
		show_str = self.__construct_trade_list_str(otc_models.otc_coincola_buy_btc_trades)
		if show_str is None:
			show_str = "CoinCola Buy BTC Data Faild"
		else:
			show_str = "CoinCola Buy BTC Data:\n" + show_str
		self.coincola_buy_btc_label.setText(show_str)

	def __show_otc_coincola_sell_btc_trades(self):
		show_str = self.__construct_trade_list_str(otc_models.otc_coincola_buy_btc_trades)
		if show_str is None:
			show_str = "CoinCola Sell BTC Data Faild"
		else:
			show_str = "CoinCola Sell BTC Data:\n" + show_str
		self.coincola_sell_btc_label.setText(show_str)

	def __show_otc_coincola_buy_eth_trades(self):
		show_str = self.__construct_trade_list_str(otc_models.otc_coincola_buy_eth_trades)
		if show_str is None:
			show_str = "CoinCola Buy ETH Data Faild"
		else:
			show_str = "CoinCola Buy ETH Data:\n" + show_str
		self.coincola_buy_eth_label.setText(show_str)

	def __show_otc_coincola_sell_eth_trades(self):
		show_str = self.__construct_trade_list_str(otc_models.otc_coincola_sell_eth_trades)
		if show_str is None:
			show_str = "CoinCola Sell ETH Data Faild"
		else:
			show_str = "CoinCola Sell ETH Data:\n" + show_str
		self.coincola_sell_eth_label.setText(show_str)

	def __show_otc_coincola_buy_bch_trades(self):
		show_str = self.__construct_trade_list_str(otc_models.otc_coincola_buy_bch_trades)
		if show_str is None:
			show_str = "CoinCola Buy BCH Data Faild"
		else:
			show_str = "CoinCola Buy BCH Data:\n" + show_str
		self.coincola_buy_bch_label.setText(show_str)

	def __show_otc_coincola_sell_bch_trades(self):
		show_str = self.__construct_trade_list_str(otc_models.otc_coincola_sell_bch_trades)
		if show_str is None:
			show_str = "CoinCola Sell BCH Data Faild"
		else:
			show_str = "CoinCola Sell BCH Data:\n" + show_str
		self.coincola_sell_bch_label.setText(show_str)



	def updateUI(self):
		while(True):
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



def quit(signum, frame):
	print("Stop All")
	sys.exit()



if __name__ == '__main__':
	signal.signal(signal.SIGINT, quit)
	signal.signal(signal.SIGTERM, quit)
	start_all_spider()
	app = QApplication(sys.argv)
	ex = otc_viewer()
	sys.exit(app.exec_())








'''


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

	
		for item in otc_models.otc_huobi_buy_btc_trades:
			str = "{0} {1}~{2} {3}\n".format(item.trader, item.min_amount, item.max_amount, item.price)
			#print(str)
			sys.stdout.write(str)
			sys.stdout.flush()
	
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

			self.__show_otc_huobi_sell_btc_trades()
			self.__show_otc_huobi_buy_usdt_trades()
			self.__show_otc_huobi_sell_usdt_trades()
			self.__show_otc_coincola_buy_btc_trades()
			self.__show_otc_coincola_sell_btc_trades()
			self.__show_otc_coincola_buy_eth_trades()
			self.__show_otc_coincola_sell_eth_trades()
			self.__show_otc_coincola_buy_bch_trades()
			self.__show_otc_coincola_sell_bch_trades()
			
			time.sleep(2)
'''