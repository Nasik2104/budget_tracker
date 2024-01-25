from sqlalchemy.orm import Mapped, relationship, mapped_column

from . import Base


class ProductType(Base):
    name: Mapped['str'] = mapped_column(unique=True)
    description: Mapped['str']
    products: Mapped[list["products"]] = relationship('Product', back_populates='product_type')

