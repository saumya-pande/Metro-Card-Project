from collections import defaultdict

class Station:
    def __init__(self, place):
        self.place = place
        self.total_amount = 0
        self.discount = 0
        self.passenger_history = defaultdict(int)

    def add_amount(self, amount):
        self.total_amount += amount

    def update_discount(self, disc):
        self.discount += disc

    def add_passenger_history(self, type):
        self.passenger_history[type] +=1

