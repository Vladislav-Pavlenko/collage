from datetime import datetime


def validateRow(func):
    def wrapper(self, *args, **kwargs):
        row = args[2]
        if row > 15:
            raise ValueError("The row value must be less than or equal to 15")
        return func(self, *args, **kwargs)
    return wrapper


class Tickets():
    @validateRow
    def __init__(self, seansDate, seansTime, row):
        self.seansDate = seansDate
        self.seansTime = seansTime
        self.row = row

    def ticketPrice(self):
        if self.seansTime >= 10 and self.seansTime <=17:
            price = (15+1.5)*self.row
            return f"Price your tickets: {price}"
        elif self.seansTime >= 18 and self.seansTime <=22:
            price = (25+2) * self.row
            return f"Price your tickets: {price}"

        else:
            return "The cinema is not working"
date  = datetime.now()
obj = Tickets(date, 22, 1)
print(obj.ticketPrice())
# Tickets(123, 23, 56)