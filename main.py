# coding: utf-8

import time, sys, signal

from otc_model import *
from data_downloader import *


otc_huobi_buy_btc_ads = []
otc_huobi_sell_btc_ads = []
otc_huobi_buy_usdt_ads = []
otc_huobi_sell_usdt_ads = []
otc_coincola_buy_btc_ads = []
otc_coincola_sell_btc_ads = []
otc_coincola_buy_eth_ads = []
otc_coincola_sell_eth_ads = []

downloaders = []


ad = otc_huobi_ad(otc_coin_type.BTC, otc_trade_type.Buy)
cc_ad = otc_coincola_ad(otc_coin_type.BTC, otc_trade_type.Buy)

ad.set_data("fredshao",132,5000,100000,11457.28)
cc_ad.set_data("halan",125,89,1000,20000,11543.89)

print(ad.get_show_str())
print(cc_ad.get_show_str())


def callback():
	print("Call back from thread")


huobi_downloader = downloader("http://otc.huobi.pro",2,callback)

downloaders.append(huobi_downloader)


def quit(signum, frame):
	print("Stop All")
	sys.exit()


if __name__ == '__main__':
	try:
		signal.signal(signal.SIGINT, quit)
		signal.signal(signal.SIGTERM, quit)

		for downloader in downloaders:
			downloader.start()

		while True:
			pass

	except Exception as exe:
		print(exe)


