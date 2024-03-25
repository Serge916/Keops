from meeting import *
from random import choice


class Round:
    def __init__(
        self,
        agents: list[Agent] = None,
        matchingStrategy: int = RANDOM,
    ) -> None:
        self.buyers = [i for i in agents if i.type == BUYER]
        self.sellers = [i for i in agents if i.type == SELLER]
        self.roundCount = 1
        self.__runRound(matchingStrategy)
        self.matchedPairs = set()

    def __runRound(self, matchingStrategy):
        for i in range(min(len(self.buyers), len(self.sellers))):
            if matchingStrategy == RANDOM:
                buyer = choice(self.buyers)
                seller = choice(self.sellers)
            else:
                # TODO: Implement other matching strategies

                # Strategy one: No two pairs of buyers and sellers are matched again
                availableBuyers = [
                    buyer for buyer in self.buyers if buyer not in self.matchedPairs
                ]
                availableSellers = [
                    seller for seller in self.sellers if seller not in self.matchedPairs
                ]
                if availableBuyers and availableSellers:
                    buyer = choice(availableBuyers)
                    seller = choice(availableSellers)
                else:
                    # Break if no available buyers and sellers
                    break

            Meeting(buyer, seller)
            self.matchedPairs.add(buyer)
            self.matchedPairs.add(seller)

            if buyer.success:
                self.buyers.remove(buyer)

            if seller.success:
                self.sellers.remove(seller)

        self.roundCount += 1
