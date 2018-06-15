import sys

from urllib.request import urlopen

from lxml import etree

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QDoubleSpinBox, QVBoxLayout, QPushButton

class Course(QObject):
	CBR_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
	def get(self):
		with urlopen(self.CBR_URL) as f:
			tree = etree.parse(f)
			value = tree.xpath('*[@ID="R01235"]/Value')[0].text
			return float(value.replace(',', '.'))


class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._initUi()
		self._initSignals()
		self._initLayouts()
	
	def _initUi(self):
		self.setWindowTitle('Конвертер валют')
		
		self.srcLabel = QLabel('Сумма в рублях', self)
		self.resultLabel = QLabel('Сумма в долларах', self)
		
		# Для ввода числа
		self.srcAmountRub = QDoubleSpinBox(self)
		self.srcAmountRub.setMaximum(99999999)
		
		self.srcAmountDollar = QDoubleSpinBox(self)
		self.srcAmountDollar.setMaximum(99999999)
		
		self.convertBtn = QPushButton('Перевести', self)
		self.resetBtn = QPushButton('Сброс', self)
	
	def _initSignals(self):
		# Принимаем сигналы и вызываем функции по ним
		self.convertBtn.clicked.connect(self.onClickConvertBtn)
		self.resetBtn.clicked.connect(self.onClickResetBtn)
	
	def _initLayouts(self):
		w = QWidget(self)
		# Родительскую(self) передавать не нужно ему 
		self.MainLayout = QVBoxLayout(w)
		
		self.MainLayout.addWidget(self.srcLabel)
		self.MainLayout.addWidget(self.srcAmountRub)
		self.MainLayout.addWidget(self.resultLabel)
		self.MainLayout.addWidget(self.srcAmountDollar)
		self.MainLayout.addWidget(self.convertBtn)
		self.MainLayout.addWidget(self.resetBtn)
		
		self.setCentralWidget(w)
	
	def onClickConvertBtn(self):
		valueRub = self.srcAmountRub.value()
		valueDollar = self.srcAmountDollar.value()
		
		if (valueRub and valueDollar) or not (valueRub and valueDollar):
			self.convertBtn.setEnabled(False)
			self.convertBtn.setEnabled(True)
		
		if valueRub and not valueDollar:
			self.srcAmountDollar.setValue(valueRub / Course().get())
		
		if valueDollar and not valueRub:
			self.srcAmountRub.setValue(valueDollar * Course().get())
	
	def onClickResetBtn(self):
		self.srcAmountDollar.setValue(0.00)
		self.srcAmountRub.setValue(0.00)
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	converter = MainWindow()
	converter.show()
	
	sys.exit(app.exec_())
