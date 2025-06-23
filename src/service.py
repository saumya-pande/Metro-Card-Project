from unittest.mock import AsyncMock
from .MetroCard import MetroCard, Fare
from .repository import *
from .Station import Station

#services provmided: 1. check balance of card  2. recharge card 3. print summary -> tot collection, passenger type summary

class MetroService:
    def __init__(self):
        self.metroCard = {}
        self.stations = {
            "CENTRAL": Station("Central"),
            "AIRPORT": Station("Airport")
        }

    def create_card(self, mid, balance):
        metroCard[mid] = MetroCard(mid, int(balance))

    def recharge(self, card, amount, station_name):
        card.add_balance(amount)
        station = self.stations[station_name]
        service_fee = 0.02 * amount
        station.add_amount(service_fee)

    def check_in(self, mid, type, source):
        card= self.metroCard[mid]
        is_round_trip = False
        if(card.source == "AIRPORT" and source == "CENTRAL") or (card.souce == "CENTRAL" and source == "AIRPORT"):
            is_round_trip = True

        cost = Fare.get_fare(type, is_round_trip)
        station = self.stations[source]

        if card.balance < cost:
            self.recharge(mid, cost-card.balance, source)

        #update balance
        card.add_balance(cost*-1)
        if is_round_trip:
            mid.update_source(None)
            station.update_discount(cost)
        else:
            mid.update_source(source)

        station.add_amount(cost)
        station.add_passenger_history(type)

    def print_summary(self):
        for station_name in ["CENTRAL", "AIRPORT"]:
            output = []
            station = self.stations[station_name]
            output.append(f"TOTAL_COLLECTION {station_name} {int(station.total_ammount)} {int(station.discount)}")
            output.append("PASSENGER_TYPE_SUMMARY")
            #printing passenger types
            for passenger_type in sorted(station.passenger_history.items()):
                output.append(f"{passenger_type[0]} {passenger_type[1]}")

        return "/n".join(output)