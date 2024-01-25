from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

# self.__class__.__name__ + "s"

class Base(DeclarativeBase):
    @classmethod
    @property
    def __tablename__(cls)->str:
        return str(cls.__name__).lower() + "s"

    id: Mapped[int] = mapped_column(primary_key=True)
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"

from .products import Product
from .customers import Customer
from .sales import Sale
from .supliers import Suplier
from .product_types import ProductType