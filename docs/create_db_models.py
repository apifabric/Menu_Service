import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Set up the database
db_path = 'system/genai/temp/model.sqlite'
os.makedirs(os.path.dirname(db_path), exist_ok=True)
engine = create_engine(f'sqlite:///system/genai/temp/create_db_models.sqlite')
Base = declarative_base()

class Restaurant(Base):
    """description: Table to store information about different restaurants."""
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String)

class Category(Base):
    """description: Table to store categories of menu items (e.g., appetizer, chicken, etc.)."""
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class MenuItem(Base):
    """description: Table to store menu items including photo, price, and description."""
    __tablename__ = 'menu_item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    photo = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    category = relationship('Category')
    restaurant = relationship('Restaurant')

# Additional tables here, defined with descriptions

class Customer(Base):
    """description: Table to store customer information."""
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String)

class Order(Base):
    """description: Table to store customer orders."""
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    order_date = Column(DateTime, default=datetime.now)
    customer = relationship('Customer')
    restaurant = relationship('Restaurant')

class OrderItem(Base):
    """description: Table to store items within orders."""
    __tablename__ = 'order_item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    menu_item_id = Column(Integer, ForeignKey('menu_item.id'))
    quantity = Column(Integer, nullable=False)
    order = relationship('Order')
    menu_item = relationship('MenuItem')

class Supplier(Base):
    """description: Table to store suppliers for menu items."""
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)

class MenuItemSupplier(Base):
    """description: Table to map menu items to suppliers."""
    __tablename__ = 'menu_item_supplier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    menu_item_id = Column(Integer, ForeignKey('menu_item.id'))
    supplier_id = Column(Integer, ForeignKey('supplier.id'))
    menu_item = relationship('MenuItem')
    supplier = relationship('Supplier')

class Promotion(Base):
    """description: Table to store promotional offers."""
    __tablename__ = 'promotion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    discount_percentage = Column(Float)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

class MenuItemPromotion(Base):
    """description: Table to map menu items to promotions."""
    __tablename__ = 'menu_item_promotion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    menu_item_id = Column(Integer, ForeignKey('menu_item.id'))
    promotion_id = Column(Integer, ForeignKey('promotion.id'))
    menu_item = relationship('MenuItem')
    promotion = relationship('Promotion')

class Employee(Base):
    """description: Table to store restaurant employees."""
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    role = Column(String)
    email = Column(String)
    restaurant = relationship('Restaurant')

class Review(Base):
    """description: Table to store customer reviews for menu items."""
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    menu_item_id = Column(Integer, ForeignKey('menu_item.id'))
    review_text = Column(Text)
    rating = Column(Integer)
    review_date = Column(DateTime, default=datetime.now)
    customer = relationship('Customer')
    menu_item = relationship('MenuItem')

# Create all tables
Base.metadata.create_all(engine)
# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add sample data
s1 = Supplier(name="Local Farm", contact_info="localfarm@example.com")
s2 = Supplier(name="Fresh Foods Inc.", contact_info="freshfoods@example.com")
session.add_all([s1, s2])

c1 = Category(name="Appetizer")
c2 = Category(name="Main Course")
session.add_all([c1, c2])

r1 = Restaurant(name="The Gourmet Place", location="123 Main Street")
r2 = Restaurant(name="Ocean's Delight", location="456 Seaside Ave")
session.add_all([r1, r2])

m1 = MenuItem(name="Spring Rolls", description="Crispy spring rolls with veggies", price=5.99, category=c1, restaurant=r1)
m2 = MenuItem(name="Grilled Salmon", description="Salmon fillet with herbs", price=18.50, category=c2, restaurant=r2)
session.add_all([m1, m2])

session.commit()

# More sample data...
promotion1 = Promotion(name="Summer Sale", discount_percentage=10, start_date=datetime(2023, 6, 1), end_date=datetime(2023, 8, 31))
session.add(promotion1)

customer1 = Customer(name="John Doe", email="johndoe@example.com")
session.add(customer1)

order1 = Order(customer=customer1, restaurant=r1, order_date=datetime.now())
session.add(order1)

order_item1 = OrderItem(order=order1, menu_item=m1, quantity=2)
session.add(order_item1)

review1 = Review(customer=customer1, menu_item=m1, review_text="Very tasty!", rating=5)
session.add(review1)

employee1 = Employee(name="Alice Chef", restaurant=r1, role="Chef", email="alice@example.com")
session.add(employee1)

# More sample data entries for other tables...

# Commit the session to save data to the database
session.commit()

# Close the session
session.close()
