from agents import *

# Simulation parameters
DAYS = 3


def interact(buyer: Agent, seller: Agent) -> None:
    if buyer.strategy == NEGOTIATE:
        pass
    if buyer.strategy == WALKBY:
        seller.attended = True
        buyer.attended = True
        if seller.currentPrice <= buyer.priceLimit:
            print("Agents agreed on a price!")
            seller.streak += 1
            seller.success = True
            buyer.success = True

        else:
            print("Agents couldn't agree on a price")
            seller.streak -= 1


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

        interact(buyer, seller)
