# _*_ coding:utf-8 _*_

import sys, signal
from otc_data_spider import *
from otc_data_parser import *
from otc_models import *
from otc_view import *
from otc_url_consts import *


def on_otc_huobi_buy_btc_data(json_str):
	trades = parse_otc_huobi_trade_data(json_str)
	set_otc_huobi_buy_btc_trades(trades)

def on_otc_huobi_sell_btc_data(json_str):
	trades = parse_otc_huobi_trade_data(json_str)
	set_otc_huobi_sell_btc_trades(trades)

def on_otc_huobi_buy_usdt_data(json_str):
	trades = parse_otc_huobi_trade_data(json_str)
	set_otc_huobi_buy_usdt_trades(trades)

def on_otc_huobi_sell_usdt_data(json_str):
	trades = parse_otc_huobi_trade_data(json_str)
	set_otc_huobi_sell_usdt_trades(trades)

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


def start_all_spider():
	spider = otc_spider(url_otc_huobi_buy_btc, 1, on_otc_huobi_buy_btc_data)
	spider.start()

	spider = otc_spider(url_otc_huobi_sell_btc, 1, on_otc_huobi_sell_btc_data)
	spider.start()

	spider = otc_spider(url_otc_huobi_buy_usdt, 1, on_otc_huobi_buy_usdt_data)
	spider.start()

	spider = otc_spider(url_otc_huobi_sell_usdt, 1, on_otc_huobi_sell_usdt_data)
	spider.start()

	spider = otc_spider(url_otc_coincola_buy_btc, 1, on_otc_coincola_buy_btc_data)
	spider.start()

	spider = otc_spider(url_otc_coincola_sell_btc, 1, on_otc_coincola_sell_btc_data)
	spider.start()

	spider = otc_spider(url_otc_coincola_buy_eth, 1, on_otc_coincola_buy_eth_data)
	spider.start()

	spider = otc_spider(url_otc_coincola_sell_eth, 1, on_otc_coincola_sell_eth_data)
	spider.start()

	spider = otc_spider(url_otc_coincola_buy_bch, 1, on_otc_coincola_buy_bch_data)
	spider.start()

	spider = otc_spider(url_otc_coincola_sell_bch, 1, on_otc_coincola_sell_bch_data)
	spider.start()

	spider = otc_spider(url_otc_okex_buy_btc, 1, on_otc_okex_buy_btc_data)
	spider.start()

	spider = otc_spider(url_otc_okex_sell_btc, 1, on_otc_okex_sell_btc_data)
	spider.start()

	spider = otc_spider(url_otc_okex_buy_eth, 1, on_otc_okex_buy_eth_data)
	spider.start()

	spider = otc_spider(url_otc_okex_sell_eth, 1, on_otc_okex_sell_eth_data)
	spider.start()



def quit(signum, frame):
	print("Stop All")
	sys.exit()


if __name__ == '__main__':
	try:
		signal.signal(signal.SIGINT, quit)
		signal.signal(signal.SIGTERM, quit)

		start_all_spider()

		viewer = otc_viewer()
		viewer.start()

		while True:
			pass

	except Exception as exe:
		print(exe)