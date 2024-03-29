import pickle4 as pickle
import logging

from agents import *
from random import random, randrange

SUCCESSFUL_MEETING_STR = "Agents agreed on a price!"
UNSUCCESSFUL_MEETING_STR = "Agents couldn't agree on a price"

log = logging.getLogger(__name__)


class Meeting:
    classIdCounter = 0
    classStatsDf = pd.DataFrame()
    classStatsDf["day"] = pd.Series(dtype=int)
    classStatsDf["roundID"] = pd.Series(dtype=int)
    classStatsDf["meetingID"] = pd.Series(dtype=int)
    classStatsDf["buyerID"] = pd.Series(dtype=str)
    classStatsDf["sellerID"] = pd.Series(dtype=str)
    classStatsDf["success"] = pd.Series(dtype=bool)
    classStatsDf["strategy"] = pd.Series(dtype=str)
    classStatsDf["sellingPrice"] = pd.Series(dtype=float)
    classStatsDf["negotiations"] = pd.Series(dtype=int)

    """
    Agents interact based on their strategy. The Seller is the one offering the price and the Buyer agrees or rejects.
    ### Args:
        buyer (Agent): The Agent that requests the item
        seller (Agent): The Agent that offers the item
    """

    def __init__(self, buyer: Agent, seller: Agent, roundID: int, day: int) -> None:
        Meeting.classIdCounter += 1
        seller.attended = True
        buyer.attended = True
        self.roundId = roundID
        self.day = day
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
                    self.__successfulMeeting(buyer, seller, sellerPrice, tracer)
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
            self.__unsuccessfulMeeting(buyer, seller, tracer)
            return

        if buyer.strategy == STUBBORN and seller.strategy == STUBBORN:
            sellerPrice = seller.goalPrice
            if buyer.priceLimit >= seller.goalPrice:
                self.__successfulMeeting(buyer, seller, sellerPrice, 1)
                return

            self.__unsuccessfulMeeting(buyer, seller, 1)

        if buyer.strategy == STUBBORN and seller.strategy == NEGOTIATE:
            fatigue = 0
            fedUp = randrange(10, 30)
            buyerPrice = buyer.priceLimit
            sellerPrice = seller.goalPrice * (1 + randrange(0, 1))
            tracer = 0
            while fatigue < fedUp:
                tracer += 1
                if buyerPrice >= sellerPrice:
                    self.__successfulMeeting(buyer, seller, sellerPrice, tracer)
                    return
                else:
                    if sellerPrice == seller.priceLimit:
                        break

                    sellerPrice = max(sellerPrice * (1 - random()), seller.priceLimit)
                    fatigue += abs(buyerPrice - sellerPrice) * random()
            self.__unsuccessfulMeeting(buyer, seller, tracer)
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
                    self.__successfulMeeting(buyer, seller, sellerPrice, tracer)
                    return
                else:
                    if buyerPrice == buyer.priceLimit:
                        break

                    buyerPrice = min(buyerPrice * (1 + random()), buyer.priceLimit)
                    fatigue += abs(buyerPrice - sellerPrice) * random()
            self.__unsuccessfulMeeting(buyer, seller, tracer)
            return

    def __successfulMeeting(
        self, buyer: Agent, seller: Agent, sellingPrice: int, negotiations: int
    ):
        log.info(
            f"Buyer ({buyer.agentID}) and Seller ({seller.agentID}) agreed on a price of {sellingPrice} after {negotiations} negotiations."
        )
        seller.success = True
        buyer.success = True
        buyer.lastAgreedPrice = sellingPrice
        seller.lastAgreedPrice = sellingPrice

        df = pd.DataFrame(
            [
                {
                    "day": self.day,
                    "roundID": self.roundId,
                    "buyerID": buyer.agentID,
                    "sellerID": seller.agentID,
                    "success": True,
                    "sellingPrice": sellingPrice,
                    "strategy": f"S{seller.strategy}B{buyer.strategy}",
                    "negotiations": negotiations,
                    "meetingID": Meeting.classIdCounter,
                }
            ]
        )
        Meeting.classStatsDf = pd.concat([Meeting.classStatsDf, df], ignore_index=True)

    def __unsuccessfulMeeting(self, buyer: Agent, seller: Agent, negotiations: int):
        log.info(
            f"Buyer ({buyer.agentID}) and Seller ({seller.agentID}) couldn't agree on a price after {negotiations} negotiations."
        )
        df = pd.DataFrame(
            [
                {
                    "day": self.day,
                    "roundID": self.roundId,
                    "buyerID": buyer.agentID,
                    "sellerID": seller.agentID,
                    "success": False,
                    "sellingPrice": 0,
                    "strategy": f"S{seller.strategy}B{buyer.strategy}",
                    "negotiations": negotiations,
                    "meetingID": Meeting.classIdCounter,
                }
            ]
        )
        Meeting.classStatsDf = pd.concat([Meeting.classStatsDf, df], ignore_index=True)
