import logging

from meeting import *
from random import choice

log = logging.getLogger(__name__)


class Round:
    classIdCounter = 0
    classStatsDf = pd.DataFrame()
    classStatsDf["day"] = pd.Series(dtype=int)
    classStatsDf["roundID"] = pd.Series(dtype=int)
    classStatsDf["roundOfDay"] = pd.Series(dtype=int)
    classStatsDf["matchingStrat"] = pd.Series(dtype=int)

    def __init__(
        self,
        agents: list[Agent],
        roundOfDay: int,
        matchingStrategy: int = RANDOM,
        roundInDay: int = 0,
        day: int = 0,
    ) -> None:
        log.debug(
            f"Creating class Round with the following arguments numAgents: {len(agents)}, roundOfDay: {roundOfDay}, mathchingStrategy: {matchingStrategy}"
        )

        self.roundId = Round.classIdCounter
        Round.classIdCounter += 1
        self.buyers = [i for i in agents if i.type == BUYER]
        self.sellers = [i for i in agents if i.type == SELLER]
        self.roundInDay = roundInDay
        self.day = day
        self.matchedPairs = set()
        self.numMeetings = min(len(self.buyers), len(self.sellers))
        log.info(
            f"In total there are {self.buyers} buyers and {self.sellers}. So total number of meetings: {self.numMeetings}"
        )
        self.__runRound(matchingStrategy)
        self.__getStats(matchingStrategy)
        Round.classIdCounter += 1

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

            Meeting(buyer, seller, roundID=Round.classIdCounter, day=self.day)
            self.matchedPairs.add(buyer)
            self.matchedPairs.add(seller)

            if buyer.success:
                self.buyers.remove(buyer)

            if seller.success:
                self.sellers.remove(seller)

    def __getStats(self, matchingStrat):
        df = pd.DataFrame(
            [
                {
                    "day": self.day,
                    "roundID": Round.classIdCounter,
                    "roundOfDay": self.roundInDay,
                    "matchingStrat": matchingStrat,
                }
            ]
        )
        Round.classStatsDf = pd.concat([Round.classStatsDf, df], ignore_index=True)
