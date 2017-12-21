# -*- coding:utf-8 -*-

class currency(object):
	def __init__(self,name):
		self.name = name
		self.trade_balance = 0.0
		self.frozen_balance = 0.0

	def update_trade_balance(self,balance):
		self.trade_balance = balance

	def update_frozen_balance(self,balance):
		self.frozen_balance = balance