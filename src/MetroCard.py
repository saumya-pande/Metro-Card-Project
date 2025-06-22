# class MetroCard:
#     def __init__(self, line):
#         self.line = line
#         words = line.split()
#         self.command = words[0]
#         if self.command == "BALANCE":
#             self.cardNumber = words[1]
#             self.value = words[2]
#         if self.command == "CHECK_IN":
#             self.cardNumber = words[1]
#             self.place = lambda x: x for x in words[2:]
#         else:
#             printSummary()

class MetroCard:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
        self.source = None #this is the station from where the person is travelling

    def add_balance(self, balance):
        self.balance += balance

    def update_source(self, source):
        self.source = source

