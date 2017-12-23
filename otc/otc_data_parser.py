# coding: utf-8
from otc_models import *

# 1 buy, 0 sell, 1 btc, 2 usdt
def parse_otc_huobi_trade_data(json_str):
	if(json_str is None):
		return None
	trade_list = []
	for item in json_str['data']:
		user_name = item['userName']
		price = item['price']
		min_amount = item['minTradeLimit']
		max_amount = item['maxTradeLimit']
		trade = otc_trade()
		trade.set_data(user_name, price, min_amount,max_amount)
		trade_list.append(trade)
	return trade_list



def parse_otc_coincola_trade_data(json_str):
	if(json_str is None):
		return None
	trade_list = []
	for item in json_str['data']['advertisements']:
		if(item['advertiser']['state'] != 'ONLINE'):
			continue

		name = item['advertiser']['name']
		price = item['price']
		min_amount = item['min_amount']
		max_amount = item['max_amount']

		trade = otc_trade()
		trade.set_data(name, price, min_amount,max_amount)
		trade_list.append(trade)

	return trade_list


def parse_otc_okex_trade_data(json_str):
	pass