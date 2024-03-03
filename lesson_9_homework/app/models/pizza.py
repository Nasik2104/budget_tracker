from sqlalchemy.orm import Mapped, mapped_column
from . import Base

class Pizza(Base):
    name: Mapped['str'] = mapped_column(unique=True)
    price: Mapped['str']
    image_link: Mapped['str']
    ingredients: Mapped['str']

class Feedbacks(Base):
    mark: Mapped['int'] = mapped_column()
    name: Mapped['str'] = mapped_column()
    email: Mapped['str'] = mapped_column()
    message: Mapped['str'] = mapped_column()
    color: Mapped['str'] = mapped_column()