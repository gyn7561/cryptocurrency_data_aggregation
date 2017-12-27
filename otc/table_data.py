from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QTableWidget, QTableWidgetItem, QAbstractItemView, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys


class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
		self.createTableItem()

	def initUI(self):
		self.setWindowTitle("Table Test")
		self.setGeometry(100,100,800,600)

		tableItems = self.createTableItem()
		table1 = self.createTableView(tableItems)

		self.layout = QGridLayout()
		self.layout.setSpacing(0)
		self.layout.addWidget(table1,0,0)
		self.setLayout(self.layout)

		self.show()



	def createTableItem(self):
		row = []
		for x in range(10):
			col = []
			for y in range(4):
				item = QTableWidgetItem(str(x) + "_" + str(y))
				col.append(item)
			row.append(col)
		return row


	def createTableView(self, table_data):
		row = 10
		col = 4
		rowHeight = 20
		colWidth0 = 120

		tableWidget = QTableWidget()
		tableWidget.setFocusPolicy(Qt.NoFocus)
		tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		tableWidget.horizontalHeader().hide()
		tableWidget.verticalHeader().hide()
		tableWidget.setRowCount(row)
		tableWidget.setColumnCount(col)

		tableWidget.setColumnWidth(0,colWidth0)
		for x in range(row):
			tableWidget.setRowHeight(x,rowHeight)

		for r in range(row):
			for c in range(col):
				tableWidget.setItem(r,c, table_data[r][c])

		return tableWidget

'''
	def createTable(self):
		tableWidget = QTableWidget()
		tableWidget.setFocusPolicy(Qt.NoFocus)
		tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		tableWidget.horizontalHeader().hide()
		tableWidget.verticalHeader().hide()
		tableWidget.setRowCount(10)
		tableWidget.setColumnCount(4)

		tableWidget.setColumnWidth(0,120)
		for x in range(10):
			tableWidget.setRowHeight(x,20)


		item = QTableWidgetItem()
		item.setText("test")
		tableWidget.setItem(0,0,item)
		tableWidget.setItem(0,1, QTableWidgetItem("111"))
		tableWidget.setItem(1,2, QTableWidgetItem("haha"))
		tableWidget.move(0,0)
		return tableWidget
'''

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())