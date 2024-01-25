from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base

association_table = Table('customer_product_association', Base.metadata,
    Column('customer_id', ForeignKey('customers.id')),
    Column('product_id', ForeignKey('products.id')),
    extend_existing=True
)

class Customer(Base):
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    products: Mapped[list['products']] = relationship('Product', secondary=association_table, back_populates='customers')
