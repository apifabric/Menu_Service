# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 14, 2024 17:24:39
# Database: sqlite:////tmp/tmp.f3JBegfI7a/Menu_Service/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Category(SAFRSBaseX, Base):
    """
    description: Table to store categories of menu items (e.g., appetizer, chicken, etc.).
    """
    __tablename__ = 'category'
    _s_collection_name = 'Category'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    MenuItemList : Mapped[List["MenuItem"]] = relationship(back_populates="category")



class Customer(SAFRSBaseX, Base):
    """
    description: Table to store customer information.
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="customer")



class Promotion(SAFRSBaseX, Base):
    """
    description: Table to store promotional offers.
    """
    __tablename__ = 'promotion'
    _s_collection_name = 'Promotion'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    discount_percentage = Column(Float)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    MenuItemPromotionList : Mapped[List["MenuItemPromotion"]] = relationship(back_populates="promotion")



class Restaurant(SAFRSBaseX, Base):
    """
    description: Table to store information about different restaurants.
    """
    __tablename__ = 'restaurant'
    _s_collection_name = 'Restaurant'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    EmployeeList : Mapped[List["Employee"]] = relationship(back_populates="restaurant")
    MenuItemList : Mapped[List["MenuItem"]] = relationship(back_populates="restaurant")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="restaurant")



class Supplier(SAFRSBaseX, Base):
    """
    description: Table to store suppliers for menu items.
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    MenuItemSupplierList : Mapped[List["MenuItemSupplier"]] = relationship(back_populates="supplier")



class Employee(SAFRSBaseX, Base):
    """
    description: Table to store restaurant employees.
    """
    __tablename__ = 'employee'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    restaurant_id = Column(ForeignKey('restaurant.id'))
    role = Column(String)
    email = Column(String)

    # parent relationships (access parent)
    restaurant : Mapped["Restaurant"] = relationship(back_populates=("EmployeeList"))

    # child relationships (access children)



class MenuItem(SAFRSBaseX, Base):
    """
    description: Table to store menu items including photo, price, and description.
    """
    __tablename__ = 'menu_item'
    _s_collection_name = 'MenuItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    photo = Column(String)
    category_id = Column(ForeignKey('category.id'))
    restaurant_id = Column(ForeignKey('restaurant.id'))

    # parent relationships (access parent)
    category : Mapped["Category"] = relationship(back_populates=("MenuItemList"))
    restaurant : Mapped["Restaurant"] = relationship(back_populates=("MenuItemList"))

    # child relationships (access children)
    MenuItemPromotionList : Mapped[List["MenuItemPromotion"]] = relationship(back_populates="menu_item")
    MenuItemSupplierList : Mapped[List["MenuItemSupplier"]] = relationship(back_populates="menu_item")
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="menu_item")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="menu_item")



class Order(SAFRSBaseX, Base):
    """
    description: Table to store customer orders.
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    restaurant_id = Column(ForeignKey('restaurant.id'))
    order_date = Column(DateTime)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))
    restaurant : Mapped["Restaurant"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="order")



class MenuItemPromotion(SAFRSBaseX, Base):
    """
    description: Table to map menu items to promotions.
    """
    __tablename__ = 'menu_item_promotion'
    _s_collection_name = 'MenuItemPromotion'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    menu_item_id = Column(ForeignKey('menu_item.id'))
    promotion_id = Column(ForeignKey('promotion.id'))

    # parent relationships (access parent)
    menu_item : Mapped["MenuItem"] = relationship(back_populates=("MenuItemPromotionList"))
    promotion : Mapped["Promotion"] = relationship(back_populates=("MenuItemPromotionList"))

    # child relationships (access children)



class MenuItemSupplier(SAFRSBaseX, Base):
    """
    description: Table to map menu items to suppliers.
    """
    __tablename__ = 'menu_item_supplier'
    _s_collection_name = 'MenuItemSupplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    menu_item_id = Column(ForeignKey('menu_item.id'))
    supplier_id = Column(ForeignKey('supplier.id'))

    # parent relationships (access parent)
    menu_item : Mapped["MenuItem"] = relationship(back_populates=("MenuItemSupplierList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("MenuItemSupplierList"))

    # child relationships (access children)



class OrderItem(SAFRSBaseX, Base):
    """
    description: Table to store items within orders.
    """
    __tablename__ = 'order_item'
    _s_collection_name = 'OrderItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'))
    menu_item_id = Column(ForeignKey('menu_item.id'))
    quantity = Column(Integer, nullable=False)

    # parent relationships (access parent)
    menu_item : Mapped["MenuItem"] = relationship(back_populates=("OrderItemList"))
    order : Mapped["Order"] = relationship(back_populates=("OrderItemList"))

    # child relationships (access children)



class Review(SAFRSBaseX, Base):
    """
    description: Table to store customer reviews for menu items.
    """
    __tablename__ = 'review'
    _s_collection_name = 'Review'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    menu_item_id = Column(ForeignKey('menu_item.id'))
    review_text = Column(Text)
    rating = Column(Integer)
    review_date = Column(DateTime)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("ReviewList"))
    menu_item : Mapped["MenuItem"] = relationship(back_populates=("ReviewList"))

    # child relationships (access children)
