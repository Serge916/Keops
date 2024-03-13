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