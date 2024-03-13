from agents import *
from day import *


# Simulation parameters
DAYS = 3

class MarketSimulator():

    def __init__(self, numDays:int = 1, agents:list[Agent] = None, default_mode:int = WALKBY,  numBuyers:int = 0, numSellers:int = 0) -> None:
        pass

groupBuyers = [Agent(BUYER, WALKBY, 9, 7)]
groupSellers = [Agent(SELLER, WALKBY, 6, 6)]

for day in range(DAYS):
    for round in range(min(len(groupBuyers), len(groupSellers))):
        buyer = random.choice(groupBuyers)
        while buyer.attended == True:
            buyer = random.choice(groupBuyers)

        seller = random.choice(groupSellers)
        while seller.attended == True:
            seller = random.choice(groupSellers)

        runDay(buyer, seller)
