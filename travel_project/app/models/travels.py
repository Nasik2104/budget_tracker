from sqlalchemy.orm import Mapped, mapped_column

from datetime import date

from . import Base

class Travel(Base):
    name: Mapped['str'] = mapped_column(unique=True)
    transport: Mapped['str']
    destination: Mapped['str']
    departure: Mapped['str']
    start: Mapped['date'] = mapped_column(default=date.today())
    end: Mapped['date']
    price: Mapped['int']
    img_link: Mapped['str']
    booked: Mapped['bool'] = mapped_column(default=False)
    description: Mapped['str']