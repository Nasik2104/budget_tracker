from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base


class Sale(Base):
    product_id: Mapped['int'] = mapped_column(ForeignKey('products.id'))
    quantity_sold: Mapped['int']
    sale_date: Mapped['datetime']
    suplier_id: Mapped['int'] = mapped_column(ForeignKey('supliers.id'))
    suplier = relationship('Suplier', back_populates='sales')