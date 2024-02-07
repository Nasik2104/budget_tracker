from sqlalchemy.orm import Mapped, mapped_column
from . import Base

class Pizza(Base):
    name: Mapped['str'] = mapped_column(unique=True)
    price: Mapped['str']
    image_link: Mapped['str']
    ingredients: Mapped['str']