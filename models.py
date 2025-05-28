from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Business(Base):
    __tablename__ = 'businesses'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    total_budget = Column(Float, nullable=False)
    description = Column(String)
    resources = relationship('Resource', back_populates='business')

class Resource(Base):
    __tablename__ = 'resources'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    budget = Column(Float, nullable=False)
    description = Column(String)
    business_id = Column(Integer, ForeignKey('businesses.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    business = relationship('Business', back_populates='resources')
    category = relationship('Category', back_populates='resources')

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    resources = relationship('Resource', back_populates='category')
