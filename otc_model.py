# coding: utf-8
'''
coin_type: 1 BTC , 2 ETH, 3 USDT
trade_type: 0 Sell ,1 Buy

'''

from enum import Enum

url_otc_huobi_buy_btc = ""
url_otc_huobi_sell_btc = ""
url_otc_huobi_buy_usdt = ""
url_otc_huobi_sell_usdt = ""
url_otc_coincola_buy_btc = ""
url_otc_coincola_sell_btc = ""
url_otc_coincola_buy_eth = ""
url_otc_coincola_sell_eth = ""


class otc_coin_type(Enum):
	BTC = 1
	ETH = 2
	USDT = 3

class otc_trade_type(Enum):
	Buy = 1
	Sell = 2


class otc_huobi_ad(object):
	def __init__(self, coin_type, trade_type):
		self.coin_type = coin_type
		self.trade_type = trade_type
		self.advertiser = ""
		self.trade_count = 0
		self.min_amount = 0
		self.max_amount = 0
		self.price = 0.0

	def set_data(self,advertiser, trade_count, min_amount, max_amount, price):
		self.advertiser = advertiser
		self.trade_count = trade_count
		self.min_amount = min_amount
		self.max_amount = max_amount
		self.price = price

	def get_show_str(self):
		f_name = '{:^10}'.format(self.advertiser)
		f_trade_count = '{:^10}'.format(self.trade_count)
		f_amount = "{0}~{1}".format(self.min_amount, self.max_amount)
		f_amount = '{:^15}'.format(f_amount)
		f_price = '{:^10}'.format(self.price)
		return "{0} {1} {2} {3}".format(f_name, f_trade_count, f_amount, f_price)


class otc_coincola_ad(object):
	def __init__(self, coin_type, trade_type):
		self.coin_type = coin_type
		self.trade_type = trade_type
		self.advertiser = ""
		self.trade_count = 0
		self.trusted_count = 0
		self.min_amount = 0
		self.max_amount = 0
		self.price = 0.0

	def set_data(self, advertiser, trade_count, trusted_count, min_amount, max_amount, price):
		self.advertiser = advertiser
		self.trade_count = trade_count
		self.trusted_count = trusted_count
		self.min_amount = min_amount
		self.max_amount = max_amount
		self.price = price

	def get_show_str(self):
		f_name = '{:^10}'.format(self.advertiser)
		f_trade_count = '{:^10}'.format(self.trade_count)
		f_amount = "{0}~{1}".format(self.min_amount, self.max_amount)
		f_amount = '{:^15}'.format(f_amount)
		f_price = '{:^10}'.format(self.price)
		return "{0} {1} {2} {3}".format(f_name, f_trade_count, f_amount, f_price)


def create_otc_huobi_ad(json_str):
	print("Create otc huobi ad")

def create_otc_coincola_ad(json_str):
	print("Create otc coincola ad")