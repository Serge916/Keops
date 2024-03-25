from meeting import *
from random import choice


class Round:
    def __init__(
        self,
        buyers: list[Agent] = None,
        sellers: list[Agent] = None,
        matchingStrategy: int = RANDOM,
    ) -> None:
        self.buyers = buyers
        self.sellers = sellers
        self.roundCount = 0
        self.runRound(matchingStrategy)

    def runRound(self, matchingStrategy):
        for i in range(min(len(self.buyers), len(self.sellers))):
            if matchingStrategy == RANDOM:
                buyer = choice(self.buyers)
                seller = choice(self.sellers)
            else:
                # TODO Review
                pass

            Meeting(buyer, seller)

            if buyer.success == True:
                self.buyers.remove(buyer)

            if seller.success == True:
                self.sellers.remove(seller)

        self.roundCount += 1
