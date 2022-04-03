import sqlite3
import pandas as pd

con = sqlite3.connect('data.db')
cur = con.cursor()

class User:
    def __init__(self, name):
        self.name = name

    def buy_seat(self, seat):
        pass

    def use_card(self, card, prize):
        if card.validate():
            current_balance = cur.execute("select balance from cards where number = self.card.number")



class Seat:

    def __init__(self, seat):
        self.seat = seat

    def is_free(self):
        seat_f = cur.execute(f"select taken from cinema where seat_id = '{self.seat}'").fetchone()[0]
        print(seat_f)
        if seat_f == '1':
            return False
        else:
            return True

    def occupy(self):
        if self.is_free():
            cur.execute(f"update cinema set taken = 1 where seat_id = '{self.seat}'")
            cur.execute('commit')
            print(f'seat {self.seat} changed from free to occupied')
        else:
            print('Seat is currently occupied')


class Card:

    def __init__(self, tipo, number, cvc, holder):
        self.tipo = tipo
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def __repr__(self):
        return f'Card tipo {self.tipo}, con numero {self.number} y cvc {self.cvc} ' \
               f'cuyo titular se llama {self.holder}'

    def validate(self):
        valid = cur.execute(f"""select * from cards where type = '{self.tipo}' and number = {self.number} 
                            and cvc = {self.cvc} and holder = '{self.holder}'""").fetchall()

        if len(valid) > 0:
            return True
        else:
            return False


class Ticket:
    def __init__(self, id, user, price, seat):
        self.id = id
        self.user = user
        self.price = price
        self.seat = seat

    def to_pdf(self, path):
        pass

user = User(name='Francisco Donaire')
seat = Seat(seat='B3')
seat2 = Seat(seat='B2')
card = Card(tipo='Master Card', number=23456789, cvc=234, holder='Marry Smith')
seat.occupy()
seat2.occupy()