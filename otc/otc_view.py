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
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QTableWidget, QTableWidgetItem, QAbstractItemView, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtGui import QFont
from otc_main import *


class viewer_ticker(QThread):
	updated = pyqtSignal()

	def run(self):
		while(True):
			print("emit")
			self.updated.emit()
			time.sleep(1)



class otc_viewer(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

		self.ticker = viewer_ticker(self)
		self.ticker.updated.connect(self.updateUI)
		self.ticker.start()
		#self.t = threading.Thread(target=self.updateUI, name="ViewerUpdate")
		#self.t.setDaemon(True)
		#self.t.start()

	def setTableItemsHeader(self, table_data, header_text):
		table_data[0][0].setText(header_text)
		table_data[1][0].setText("Name")
		table_data[1][1].setText("Min Amount")
		table_data[1][2].setText("Max Amount")
		table_data[1][3].setText("Price")


	def createTableItems(self):
		row = []
		#row.append([QTableWidgetItem("Title")])
		for x in range(0,self.data_table_row):
			col = []
			for y in range(self.data_table_col):
				item = QTableWidgetItem(str(x) + "_" + str(y))
				col.append(item)
			row.append(col)
		return row

	def createTableView(self, table_data):
		tableWidget = QTableWidget()
		tableWidget.setFocusPolicy(Qt.NoFocus)
		tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		tableWidget.horizontalHeader().hide()
		tableWidget.verticalHeader().hide()
		tableWidget.setRowCount(self.data_table_row)
		tableWidget.setColumnCount(self.data_table_col)

		tableWidget.setColumnWidth(0, self.name_col_width)
		for x in range(self.data_table_row):
			tableWidget.setRowHeight(x,self.data_table_row_height)

		tableWidget.setRowHeight(0,30)

		tableWidget.setSpan(0,0,1,4)

		tableWidget.setItem(0,0,table_data[0][0])
		for r in range(1,self.data_table_row):
			for c in range(self.data_table_col):
				tableWidget.setItem(r,c, table_data[r][c])

		return tableWidget



	def initUI(self):
		self.data_table_row = 10 + 2
		self.data_table_col = 4
		self.name_col_width = 120
		self.data_table_row_height = 20

		self.huobi_buy_btc_table_items = self.createTableItems()
		self.setTableItemsHeader(self.huobi_buy_btc_table_items,"Huobi Buy BTC:")
		self.huobi_sell_btc_table_items = self.createTableItems()
		self.setTableItemsHeader(self.huobi_sell_btc_table_items,"Huobi Sell BTC:")
		self.huobi_buy_usdt_table_items = self.createTableItems()
		self.setTableItemsHeader(self.huobi_buy_usdt_table_items,"Huobi Buy USDT:")
		self.huobi_sell_usdt_table_items = self.createTableItems()
		self.setTableItemsHeader(self.huobi_sell_usdt_table_items,"Huobi Sell USDT:")
		self.coincola_buy_btc_table_items = self.createTableItems()
		self.setTableItemsHeader(self.coincola_buy_btc_table_items,"CoinCola Buy BTC:")
		self.coincola_sell_btc_table_items = self.createTableItems()
		self.setTableItemsHeader(self.coincola_sell_btc_table_items,"CoinCola Sell BTC:")
		self.coincola_buy_eth_table_items = self.createTableItems()
		self.setTableItemsHeader(self.coincola_buy_eth_table_items,"CoinCola Buy ETH:")
		self.coincola_sell_eth_table_items = self.createTableItems()
		self.setTableItemsHeader(self.coincola_sell_eth_table_items,"CoinCola Sell ETH:")
		self.coincola_buy_bch_table_items = self.createTableItems()
		self.setTableItemsHeader(self.coincola_buy_bch_table_items,"CoinCola Buy BCH:")
		self.coincola_sell_bch_table_items = self.createTableItems()
		self.setTableItemsHeader(self.coincola_sell_bch_table_items,"CoinCola Sell BCH:")

		self.huobi_buy_btc_table = self.createTableView(self.huobi_buy_btc_table_items)
		self.huobi_sell_btc_table = self.createTableView(self.huobi_sell_btc_table_items)
		self.huobi_buy_usdt_table = self.createTableView(self.huobi_buy_usdt_table_items)
		self.huobi_sell_usdt_table = self.createTableView(self.huobi_sell_usdt_table_items)
		self.coincola_buy_btc_table = self.createTableView(self.coincola_buy_btc_table_items)
		self.coincola_sell_btc_table = self.createTableView(self.coincola_sell_btc_table_items)
		self.coincola_buy_eth_table = self.createTableView(self.coincola_buy_eth_table_items)
		self.coincola_sell_eth_table = self.createTableView(self.coincola_sell_eth_table_items)
		self.coincola_buy_bch_table = self.createTableView(self.coincola_buy_bch_table_items)
		self.coincola_sell_bch_table = self.createTableView(self.coincola_sell_bch_table_items)

		grid = QGridLayout()
		#grid.setSpacing(0)


		grid.addWidget(self.huobi_buy_btc_table,0,0)
		grid.addWidget(self.huobi_sell_btc_table,0,1)
		grid.addWidget(self.huobi_buy_usdt_table,0,2)
		grid.addWidget(self.huobi_sell_usdt_table,0,3)
		grid.addWidget(self.coincola_buy_btc_table,1,0)
		grid.addWidget(self.coincola_sell_btc_table,1,1)
		grid.addWidget(self.coincola_buy_eth_table,1,2)
		grid.addWidget(self.coincola_sell_eth_table,1,3)
		grid.addWidget(self.coincola_buy_bch_table,2,0)
		grid.addWidget(self.coincola_sell_bch_table,2,1)


		self.setLayout(grid)

		'''
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

		'''

		#self.resize(1730,660)
		self.setFixedSize(1729,800)
		#self.setGeometry(0,0,1920,1080)
		self.setWindowTitle('OTC Data Viewer')
		self.show()

	def __clear_table_data(self,table_data):

		for r in range(2,self.data_table_row):
			for c in range(self.data_table_col):
				table_data[r][c].setText("")


	def __show_trades_in_table(self,trades, table_data):
		self.__clear_table_data(table_data)
		index = 2
		for item in trades:
			table_data[index][0].setText(item.trader)
			table_data[index][1].setText(str(item.min_amount))
			table_data[index][2].setText(str(item.max_amount))
			table_data[index][3].setText(str(item.price))
			index += 1
			#print("SetData: ", item.trader,item.min_amount,item.max_amount,item.price)
			#print("-----------------------------------------------------------")


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
		if otc_models.otc_huobi_buy_btc_trades is None:
			self.__clear_table_data(self.huobi_buy_btc_table_items)
			return
		self.__show_trades_in_table(otc_models.otc_huobi_buy_btc_trades, self.huobi_buy_btc_table_items)

		'''
		show_str = self.__construct_trade_list_str(otc_models.otc_huobi_buy_btc_trades)
		if show_str is None:
			show_str = "Huobi Buy BTC Data Faild"
		else:
			show_str = "Huobi Buy BTC Data:\n" + show_str
		self.huobi_buy_btc_label.setText(show_str)
		'''

	def __show_otc_huobi_sell_btc_trades(self):
		if otc_models.otc_huobi_sell_btc_trades is None:
			self.__clear_table_data(self.huobi_sell_btc_table_items)
			return
		self.__show_trades_in_table(otc_models.otc_huobi_sell_btc_trades, self.huobi_sell_btc_table_items)

		'''
		show_str = self.__construct_trade_list_str(otc_models.otc_huobi_sell_btc_trades)
		if show_str is None:
			show_str = "Huobi Sell BTC Data Faild"
		else:
			show_str = "Huobi Sell BTC Data:\n" + show_str
		self.huobi_sell_btc_label.setText(show_str)
		'''

	def __show_otc_huobi_buy_usdt_trades(self):
		if otc_models.otc_huobi_buy_usdt_trades is None:
			self.__clear_table_data(self.huobi_buy_usdt_table_items)
			return
		self.__show_trades_in_table(otc_models.otc_huobi_buy_usdt_trades,self.huobi_buy_usdt_table_items)
		'''
		show_str = self.__construct_trade_list_str(otc_models.otc_huobi_buy_usdt_trades)
		if show_str is None:
			show_str = "Huobi Buy USDT Data Faild"
		else:
			show_str = "Huobi Buy USDT Data:\n" + show_str
		self.huobi_buy_usdt_label.setText(show_str)
		'''

	def __show_otc_huobi_sell_usdt_trades(self):
		if otc_models.otc_huobi_sell_usdt_trades is None:
			self.__clear_table_data(self.huobi_sell_usdt_table_items)
			return
		self.__show_trades_in_table(otc_models.otc_huobi_sell_usdt_trades, self.huobi_sell_usdt_table_items)
		'''
		show_str = self.__construct_trade_list_str(otc_models.otc_huobi_sell_usdt_trades)
		if show_str is None:
			show_str = "Houbi Sell USDT Data Faild"
		else:
			show_str = "Huobi Sell USDT Data:\n" + show_str
		self.huobi_sell_usdt_label.setText(show_str)
		'''

	def __show_otc_coincola_buy_btc_trades(self):
		if otc_models.otc_coincola_buy_btc_trades is None:
			self.__clear_table_data(self.coincola_buy_btc_table_items)
			return
		self.__show_trades_in_table(otc_models.otc_coincola_buy_btc_trades,self.coincola_buy_btc_table_items)

		'''
		show_str = self.__construct_trade_list_str(otc_models.otc_coincola_buy_btc_trades)
		if show_str is None:
			show_str = "CoinCola Buy BTC Data Faild"
		else:
			show_str = "CoinCola Buy BTC Data:\n" + show_str
		self.coincola_buy_btc_label.setText(show_str)
		'''

	def __show_otc_coincola_sell_btc_trades(self):
		if otc_models.otc_coincola_sell_btc_trades is None:
			self.__clear_table_data(self.coincola_sell_btc_table_items)
			return
		self.__show_trades_in_table(otc_models.otc_coincola_sell_btc_trades, self.coincola_sell_btc_table_items)
		'''
		show_str = self.__construct_trade_list_str(otc_models.otc_coincola_buy_btc_trades)
		if show_str is None:
			show_str = "CoinCola Sell BTC Data Faild"
		else:
			show_str = "CoinCola Sell BTC Data:\n" + show_str
		self.coincola_sell_btc_label.setText(show_str)
		'''

	def __show_otc_coincola_buy_eth_trades(self):
		if otc_models.otc_coincola_buy_eth_trades is None:
			self.__clear_table_data(self.coincola_buy_eth_table_items)
			return
		self.__show_trades_in_table(otc_models.otc_coincola_buy_eth_trades,self.coincola_buy_eth_table_items)
		'''
		show_str = self.__construct_trade_list_str(otc_models.otc_coincola_buy_eth_trades)
		if show_str is None:
			show_str = "CoinCola Buy ETH Data Faild"
		else:
			show_str = "CoinCola Buy ETH Data:\n" + show_str
		self.coincola_buy_eth_label.setText(show_str)
		'''

	def __show_otc_coincola_sell_eth_trades(self):
		if otc_models.otc_coincola_sell_eth_trades is None:
			self.__clear_table_data(self.coincola_sell_eth_table_items)
			return
		self.__show_trades_in_table(otc_models.otc_coincola_sell_eth_trades,self.coincola_sell_eth_table_items)
		'''
		show_str = self.__construct_trade_list_str(otc_models.otc_coincola_sell_eth_trades)
		if show_str is None:
			show_str = "CoinCola Sell ETH Data Faild"
		else:
			show_str = "CoinCola Sell ETH Data:\n" + show_str
		self.coincola_sell_eth_label.setText(show_str)
		'''

	def __show_otc_coincola_buy_bch_trades(self):
		if otc_models.otc_coincola_buy_bch_trades is None:
			self.__clear_table_data(self.coincola_buy_bch_table_items)
			return
		self.__show_trades_in_table(otc_models.otc_coincola_buy_bch_trades, self.coincola_buy_bch_table_items)
		'''
		show_str = self.__construct_trade_list_str(otc_models.otc_coincola_buy_bch_trades)
		if show_str is None:
			show_str = "CoinCola Buy BCH Data Faild"
		else:
			show_str = "CoinCola Buy BCH Data:\n" + show_str
		self.coincola_buy_bch_label.setText(show_str)
		'''

	def __show_otc_coincola_sell_bch_trades(self):
		if otc_models.otc_coincola_sell_bch_trades is None:
			self.__clear_table_data(self.coincola_sell_bch_table_items)
			return
		self.__show_trades_in_table(otc_models.otc_coincola_sell_bch_trades, self.coincola_sell_bch_table_items)
		'''
		show_str = self.__construct_trade_list_str(otc_models.otc_coincola_sell_bch_trades)
		if show_str is None:
			show_str = "CoinCola Sell BCH Data Faild"
		else:
			show_str = "CoinCola Sell BCH Data:\n" + show_str
		self.coincola_sell_bch_label.setText(show_str)
		'''



	def updateUI(self):
		#print("Update UI")
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
		#while(True):
			
			#self.__show_otc_huobi_buy_btc_trades()
			
			#self.__show_otc_huobi_sell_btc_trades()
			#self.__show_otc_huobi_buy_usdt_trades()
			#self.__show_otc_huobi_sell_usdt_trades()
			#self.__show_otc_coincola_buy_btc_trades()
			#self.__show_otc_coincola_sell_btc_trades()
			#self.__show_otc_coincola_buy_eth_trades()
			#self.__show_otc_coincola_sell_eth_trades()
			#self.__show_otc_coincola_buy_bch_trades()
			#self.__show_otc_coincola_sell_bch_trades()
			#time.sleep(1)



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