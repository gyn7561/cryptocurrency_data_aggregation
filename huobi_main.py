# -*- coding:utf-8 -*-

from HuobiServices import *
from huobi_model import *
from decimal import Decimal
import time

otc_account_symbol = 'otc'
spot_account_symbol = 'spot'

otc_account_id = None
spot_account_id = None

spot_currency = {}
otc_currency = {}


#print(get_accounts())
#rint(get_balance(634980))
#print(get_balance(650335))

def assign_account_id():
	accounts = get_accounts()
	for account in accounts['data']:
		if(account['type'] == otc_account_symbol):
			global otc_account_id
			otc_account_id = account['id']
		if(account['type'] == spot_account_symbol):
			global spot_account_id
			spot_account_id = account['id']

	print(otc_account_id,spot_account_id)


def update_spot_balances():
	currencies = get_balance(spot_account_id)
	for item in currencies['data']['list']:
		name = item['currency']
		value_type = item['type']
		value = item['balance']
		value = Decimal(value).quantize(Decimal('0.0000'))
		if(float(value) <= 0):
			continue

		if(not spot_currency.__contains__(name)):
			new_currency = currency(name)
			spot_currency[name] = new_currency

		if(value_type == 'trade'):
			spot_currency[name].update_trade_balance(value)
		elif(value_type == 'frozen'):
			spot_currency[name].update_frozen_balance(value)

	#for(key,value) in spot_currency.items():
		#print(value.name,value.trade_balance, value.frozen_balance)

def update_otc_balances():
	currencies = get_balance(otc_account_id)
	for item in currencies['data']['list']:
		name = item['currency']
		value_type = item['type']
		value = item['balance']
		value = Decimal(value).quantize(Decimal('0.0000'))
		if(float(value) <= 0):
			continue

		if(not otc_currency.__contains__(name)):
			new_currency = currency(name)
			otc_currency[name] = new_currency

		if(value_type == 'trade'):
			otc_currency[name].update_trade_balance(value)
		elif(value_type == 'frozen'):
			otc_currency[name].update_frozen_balance(value)

	#for(key,value) in otc_currency.items():
		#print(value.name,value.trade_balance, value.frozen_balance)

def update_trade_data():
	trades = get_trade('waxbtc')
	print(trades)

def update_kline_data():
	kline_data = get_kline('bchbtc','1year',100)
	print(kline_data)

def update_depth_data():
	depth_data = get_depth('bchbtc','step0')
	print(depth_data)

if(__name__ == '__main__'):
	#assign_account_id()
	time.sleep(1)
	update_depth_data()
	#update_kline_data()
	#for x in range(100):
		#update_trade_data()
		#update_kline_data()
		#time.sleep(0.12)
	#update_spot_balances()
	#update_otc_balances()
	#print(get_trade('eosbtc'))
