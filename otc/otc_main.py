# _*_ coding:utf-8 _*_

import sys, signal
from otc_data_spider import *
from otc_data_parser import *
from otc_models import *
from otc_view import *
from otc_url_consts import *


def on_otc_huobi_buy_btc_data(json_str):
	pass

def on_otc_huobi_sell_btc_data(json_str):
	pass

def on_otc_huobi_buy_usdt_data(json_str):
	pass

def on_otc_huobi_sell_usdt_data(json_str):
	pass

def on_otc_coincola_buy_btc_data(json_str):
	pass

def on_otc_coincola_sell_btc_data(json_str):
	pass

def on_otc_coincola_buy_eth_data(json_str):
	pass

def on_otc_coincola_sell_eth_data(json_str):
	pass

def on_otc_coincola_buy_bch_data(json_str):
	pass

def on_otc_coincola_sell_bch_data(json_str):
	pass

def on_otc_okex_buy_btc_data(json_str):
	pass

def on_otc_okex_sell_btc_data(json_str):
	pass

def on_otc_okex_buy_eth_data(json_str):
	pass

def on_otc_okex_sell_eth_data(json_str):
	pass
	



def quit(signum, frame):
	print("Stop All")
	sys.exit()


if __name__ == '__main__':
	try:
		signal.signal(signal.SIGINT, quit)
		signal.signal(signal.SIGTERM, quit)

		spider = otc_spider(url,1,on_otc_data)
		spider.start()

		viewer = otc_viewer()
		viewer.start()

		while True:
			pass

	except Exception as exe:
		print(exe)