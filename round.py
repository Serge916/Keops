import logging

from meeting import *
from random import choice

log = logging.getLogger(__name__)


class Round:
    classIdCounter = 0

    def __init__(
        self,
        agents: list[Agent],
        roundOfDay: int,
        matchingStrategy: int = RANDOM,
    ) -> None:
        log.debug(
            f"Creating class Round with the following arguments numAgents: {len(agents)}, roundOfDay: {roundOfDay}, mathchingStrategy: {matchingStrategy}"
        )

        self.roundId = Round.classIdCounter
        Round.classIdCounter += 1
        self.buyers = [i for i in agents if i.type == BUYER]
        self.sellers = [i for i in agents if i.type == SELLER]
        self.roundOfDay = roundOfDay
        self.matchedPairs = set()
        self.numMeetings = min(len(self.buyers), len(self.sellers))
        log.info(
            f"In total there are {self.buyers} buyers and {self.sellers}. So total number of meetings: {self.numMeetings}"
        )
        self.__runRound(matchingStrategy)

    def __runRound(self, matchingStrategy):
        log.info(f"----- Start Round: {self.roundOfDay}. ID: {self.roundId}")

        for i in range(self.numMeetings):
            if matchingStrategy == RANDOM:
                log.debug(f"Selecting randomly")
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

            log.debug(f"Buyer selected: {buyer}. Seller selected {seller}")

            Meeting(buyer, seller)
            self.matchedPairs.add(buyer)
            self.matchedPairs.add(seller)

            if buyer.success:
                self.buyers.remove(buyer)

            if seller.success:
                self.sellers.remove(seller)

        log.info(f"----- End Round: {self.roundOfDay}\n")
