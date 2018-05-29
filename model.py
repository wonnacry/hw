from pony.orm import Database, Required, Optional, Set, PrimaryKey, db_session
from datetime import datetime

db = Database()

class Product(db.Entity):
	category = Optional('Category')
	# alt_categories = Set("Category")
	unit = Required(str)
	price = Required(float)
	description = Optional(str)
	title = Required(str)
	# amount = int
	history = Set('ProductHistory')
	cartitem = Optional('CartItem')
	orderitem = Set('OrderItem')

class ProductHistory(db.Entity):
	product = Required('Product')
	created = Optional(datetime, default=datetime.now)
	price = Required(float)

class Category(db.Entity):
	title = Required(str)
	products = Set('Product')
	parent = 'Category'


class Customer(db.Entity):
	email = Optional(str)
	phone = Optional(str)
	name = Optional(str)
	adress = list('Adress')
	cart = Required('Cart')
	order = Required('Order')

class Adress(db.Entity):
	customer = 'Customer'
	country = Optional(str)
	region = Optional(str)
	city = Optional(str)
	street = Optional(str)
	house = Optional(int)
	zip_code = Optional(str)

class Cart(db.Entity):
	customer = Optional('Customer') or None
	products = list('CartItem')
	cartitem = Required('CartItem')

class CartItem(db.Entity):
	'''Одна позиция в корзине'''
	cart = Optional('Cart')
	product = Set('Product')
	amount = Required(int)

class Order(db.Entity):
	customer = Optional('Customer')
	creator = datetime
	products = Set('OrderItem')
	status = Required('Status')

class Status(db.Entity):
	name = Required(str)
	order = Optional('Order')

class OrderItem(db.Entity):
	'''Одна позиция в заказе'''
	order = Set('Order')
	product = Set('Product')
	amount = Required(int)

class Menu:
	pass


db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

with db_session():
	t_product_1 = Product(
				unit='1 kg',
				price=1.25,
				description='Best coffe you ever see',
				title='coffe',
				)
				
	t_product_2 = Product(
				unit='0.1 gramm',
				price=1700,
				title='Cocaine',
				)
				  
	t_product_3 = Product(
				unit='1 liter',
				price=73,
				title='Bear',
				)

	t_category_1 = Category(title='first_category', products=(t_product_1, t_product_2))
	t_category_2 = Category(title='second_category', products=t_product_3)
