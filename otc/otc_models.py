# _*_ coding:utf-8 _*_

from enum import Enum

otc_huobi_buy_btc_trades = []
otc_huobi_sell_btc_trades = []
otc_huobi_buy_usdt_trades = []
otc_huobi_sell_usdt_trades = []
otc_coincola_buy_btc_trades = []
otc_coincola_sell_btc_trades = []
otc_coincola_buy_eth_trades = []
otc_coincola_sell_eth_trades = []
otc_coincola_buy_bch_trades = []
otc_coincola_sell_bch_trades = []
otc_okex_buy_btc_trades = []
otc_okex_sell_btc_trades = []
otc_okex_buy_eth_trades = []
otc_okex_sell_eth_trades = []



class otc_trade(object):
	def __init__(self):
		pass

	def set_data(self, trader ,price, min_amount, max_amount):
		self.trader = trader
		self.price = price
		self.min_amount = min_amount
		self.max_amount = max_amount


def set_otc_huobi_buy_btc_trades(trades):
	otc_huobi_buy_btc_trades = trades
	for item in otc_huobi_buy_btc_trades:
		ss = "{0} {1}~{2} {3}".format(item.trader, item.min_amount, item.max_amount, item.price)
		print(ss)

def set_otc_huobi_sell_btc_trades(trades):
	otc_huobi_sell_btc_trades = trades

def set_otc_huobi_buy_usdt_trades(trades):
	otc_huobi_buy_usdt_trades = trades

def set_otc_huobi_sell_usdt_trades(trades):
	otc_huobi_sell_usdt_trades = trades

def set_otc_coincola_buy_btc_trades(trades):
	otc_coincola_buy_btc_trades = trades

def set_otc_coincola_sell_btc_trades(trades):
	otc_coincola_sell_btc_trades = trades

def set_otc_coincola_buy_eth_trades(trades):
	otc_coincola_buy_eth_trades = trades

def set_otc_coincola_sell_eth_trades(trades):
	otc_coincola_sell_eth_trades = trades

def set_otc_coincola_buy_bch_trades(trades):
	otc_coincola_buy_bch_trades = trades

def set_otc_coincola_sell_bch_trades(trades):
	otc_coincola_sell_bch_trades = trades

def set_otc_okex_buy_btc_trades(trades):
	otc_okex_buy_eth_trades = trades

def set_otc_okex_sell_btc_trades(trades):
	otc_okex_sell_btc_trades = trades

def set_otc_okex_buy_eth_trades(trades):
	otc_okex_buy_eth_trades = trades

def set_otc_okex_sell_eth_trades(trades):
	otc_okex_sell_eth_trades = trades

