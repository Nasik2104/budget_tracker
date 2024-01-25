from sqlalchemy.orm import Mapped, relationship, mapped_column

from . import Base


class Suplier(Base):
    name: Mapped['str'] = mapped_column(unique=True)
    products: Mapped[list["products"]] = relationship('Product', back_populates='suplier')
    sales: Mapped[list["sales"]] = relationship('Sale', back_populates='suplier')
