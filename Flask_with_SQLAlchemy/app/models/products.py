from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base

association_table = Table('customer_product_association', Base.metadata,
    Column('customer_id', ForeignKey('customers.id')),
    Column('product_id', ForeignKey('products.id')),
    extend_existing=True
)

class Product(Base):
    name: Mapped['str']
    quantity_in_stock: Mapped['int']
    product_type: Mapped['str'] = relationship('ProductType', back_populates='products')
    product_type_id: Mapped['int'] = mapped_column(ForeignKey('producttypes.id'))
    customers: Mapped[list['customers']] = relationship('Customer', secondary=association_table, back_populates='products')
    suplier: Mapped['suplier'] = relationship('Suplier', back_populates='products')
    suplier_id: Mapped['int'] = mapped_column(ForeignKey('supliers.id'))

