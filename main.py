import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()

class User:
    def __init__(self, name):
        self.name = name

    def buy_seat(self, seat, card):
        if seat.is_free() and card.validate():
            price = cur.execute(f"select price from cinema where seat_id = '{seat.seat}'").fetchone()[0]
            cur_balance = cur.execute(f"select balance from cards where number = {card.number}").fetchone()[0]
            print(f'The price of the ticket is {price} and the current balance is {cur_balance}')
            cur.execute(f"update cards set balance = {cur_balance} - {price} where number = {card.number};")
            cur.execute('commit')

            seat.occupy()
        else:
            print('Please try again')

class Seat:

    def __init__(self, seat):
        self.seat = seat

    def is_free(self):
        seat_f = cur.execute(f"select taken from cinema where seat_id = '{self.seat}'").fetchone()[0]
        print(seat_f)
        if seat_f == '0':
            return True
        else:
            print('Seat is occupied')
            return False

    def occupy(self):
        cur.execute(f"update cinema set taken = 1 where seat_id = '{self.seat}'")
        cur.execute('commit')
        print(f'seat {self.seat} changed from free to occupied')



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
            print('Card is not valid')
            return False


class Ticket:
    def __init__(self, id, user, price, seat):
        self.id = id
        self.user = user
        self.price = price
        self.seat = seat

    def to_pdf(self, path):
        pass

# user = User(name='Francisco Donaire')
# seat = Seat(seat='A1')
# seat2 = Seat(seat='A2')
# card = Card(tipo='Master Card', number=23456789, cvc=234, holder='Marry Smith')
# user.buy_seat(seat=seat)
# user.use_card(card=card, seat=seat)

name = input('Enter your name: ')
user = User(name=name)
seat = input('Enter your seat: ')
seat = Seat(seat=seat)
card_type = input('Enter your card type:')
card_number = int(input('Enter your card number: '))
card_cvc = int(input('Enter your card cvc: '))
card_holder = input('Enter your card holder: ')
card = Card(tipo=card_type, number=card_number, cvc=card_cvc, holder=card_holder)
user.buy_seat(seat=seat, card=card)