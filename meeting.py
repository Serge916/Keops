from agents import *
from random import random, randrange

SUCCESSFUL_MEETING_STR = "Agents agreed on a price!"
UNSUCCESSFUL_MEETING_STR = "Agents couldn't agree on a price"


class Meeting:
    """
    Agents interact based on their strategy. The Seller is the one offering the price and the Buyer agrees or rejects.
    ### Args:
        buyer (Agent): The Agent that requests the item
        seller (Agent): The Agent that offers the item
    """

    def __init__(self, buyer: Agent, seller: Agent) -> None:
        seller.attended = True
        buyer.attended = True
        self.__interact(buyer, seller)

    def __interact(self, buyer: Agent, seller: Agent) -> None:
        """
        Agents interact based on their strategy.
        ### Args:
            buyer (Agent): The Agent that requests the item
            seller (Agent): The Agent that offers the item
        ### Flow:
            - Select strategy model
            - Set initial prices
            - Interact until fatigue runs out
            - Update lastAgreedPrice, success
        """
        if buyer.strategy == NEGOTIATE and seller.strategy == NEGOTIATE:
            fatigue = 0
            fedUp = randrange(10, 30)
            buyerPrice = buyer.goalPrice * (1 - randrange(0, 1))
            sellerPrice = seller.goalPrice * (1 + randrange(0, 1))
            tracer = 0
            while fatigue < fedUp:
                tracer += 1
                if buyerPrice >= sellerPrice:
                    print(SUCCESSFUL_MEETING_STR)
                    print(f"Negotiations: {tracer}")
                    seller.success = True
                    buyer.success = True
                    buyer.lastAgreedPrice = sellerPrice
                    seller.lastAgreedPrice = sellerPrice
                    return
                else:
                    if (
                        buyerPrice == buyer.priceLimit
                        and sellerPrice == seller.priceLimit
                    ):
                        break

                    buyerPrice = min(buyerPrice * (1 + random()), buyer.priceLimit)
                    sellerPrice = max(sellerPrice * (1 - random()), seller.priceLimit)
                    fatigue += abs(buyerPrice - sellerPrice) * random()
            print(UNSUCCESSFUL_MEETING_STR)
            return

        if buyer.strategy == STUBBORN and seller.strategy == STUBBORN:
            sellerPrice = seller.goalPrice
            if buyer.priceLimit >= seller.goalPrice:
                print(SUCCESSFUL_MEETING_STR)
                seller.success = True
                buyer.success = True
                seller.lastAgreedPrice = sellerPrice
                buyer.lastAgreedPrice = sellerPrice
                return

            print(UNSUCCESSFUL_MEETING_STR)

        if buyer.strategy == STUBBORN and seller.strategy == NEGOTIATE:
            fatigue = 0
            fedUp = randrange(10, 30)
            buyerPrice = buyer.priceLimit
            sellerPrice = seller.goalPrice * (1 + randrange(0, 1))
            tracer = 0
            while fatigue < fedUp:
                tracer += 1
                if buyerPrice >= sellerPrice:
                    print(SUCCESSFUL_MEETING_STR)
                    print(f"Negotiations: {tracer}")
                    seller.success = True
                    buyer.success = True
                    seller.lastAgreedPrice = sellerPrice
                    buyer.lastAgreedPrice = sellerPrice
                    return
                else:
                    if sellerPrice == seller.priceLimit:
                        break

                    sellerPrice = max(sellerPrice * (1 - random()), seller.priceLimit)
                    fatigue += abs(buyerPrice - sellerPrice) * random()
            print(UNSUCCESSFUL_MEETING_STR)
            return

        if buyer.strategy == NEGOTIATE and seller.strategy == STUBBORN:
            fatigue = 0
            fedUp = randrange(10, 30)
            buyerPrice = buyer.goalPrice * (1 - randrange(0, 1))
            sellerPrice = seller.goalPrice
            tracer = 0
            while fatigue < fedUp:
                tracer += 1
                if buyerPrice >= sellerPrice:
                    print(SUCCESSFUL_MEETING_STR)
                    print(f"Negotiations: {tracer}")
                    seller.success = True
                    buyer.success = True
                    seller.lastAgreedPrice = sellerPrice
                    buyer.lastAgreedPrice = sellerPrice
                    return
                else:
                    if buyerPrice == buyer.priceLimit:
                        break

                    buyerPrice = max(buyerPrice * (1 + random()), buyer.priceLimit)
                    fatigue += abs(buyerPrice - sellerPrice) * random()
            print(UNSUCCESSFUL_MEETING_STR)
            return
