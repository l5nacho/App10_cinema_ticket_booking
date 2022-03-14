class User:
    def _init__(self, name):
        self.name = name

    def buy_seat(self, seat):
        pass

    def use_card(self, card):
        pass

class Seat:

    def __init__(self, seat_id, price):
        self.seat_id = seat_id
        self.price = price

    def is_free(self):
        pass

    def occupy(self):
        pass

class Card:

    def __init__(self, tipo, number, cvc, holder):
        self.tipo = tipo
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self):
        pass

class Ticket:
    def __init__(self, id, user, price, seat):
        self.id = id
        self.user = user
        self.price = price
        self.seat = seat

    def to_pdf(self, path):
        pass