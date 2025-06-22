from unittest.mock import AsyncMock
from .MetroCard import MetroCard
from .repository import *

#services provided: 1. check balance of card  2. recharge card 3. print summary -> tot collection, passenger type summary
def balance(card, balance):
    metroCard[card] = MetroCard(card, int(balance))

def recharge(card, amount, source):
    card.add_balance(amount)
    station = stations[source]
    service_fee = 0.02 * amount
    station.add_amount(service_fee)

def check_in(card, type, source):
    curr_card = metroCard[card]
    cost = rates[type]
    station = stations[source]
    is_round_trip = False
    if(curr_card.source == "AIRPORT" && source == "CENTRAL") || (curr_card.souce == "CENTRAL" && source == "AIRPORT"):
        cost/=2
        is_round_trip = True
        station.update_discount(cost)
    if(curr_card.balance < cost)
        recharge(card, cost-curr_card.balance, source)

    #update balance
    curr_card.add_balance(cost*-1)
    if is_round_trip:
        card.update_source(None)
    else:
        card.update_source(source)

    station.add_amount(cost)
    station.add_passenger_history(type)

def print_summary():
    for station_name in ["CENTRAL", "AIRPORT"]:
        output = []
        station = stations[station_name]
        output.append(f"TOTAL_COLLECTION {station_name} {int(station.total_ammount)} {int(station.discount)}")
        output.append("PASSENGER_TYPE_SUMMARY")
        #printing passenger types
        for passenger_type in sorted(station.passenger_history.items()):
            output.append(f"{passenger_type[0]} {passenger_type[1]}")

    return "/n".join(output)

        


