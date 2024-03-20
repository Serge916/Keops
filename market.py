from random import random
import logging

from agents import *
from day import *

log = logging.getLogger(__name__)
logging.basicConfig(filename="simulator.log", filemode="a", level=logging.DEBUG)


class MarketSimulator:
    """Class that manages the whole simulation

    Args:
        numDays (int): Number of days to run the simulation for. Default=1
        agents (list[Agent]): Array of agents that participate in the market. Default=None
        defaultStrategy (int): If no agents are provided, then they will be generated with this defaultStrategy. Default=None
        numBuyers (int): Number of buyers in case the agents are generated. Default=0
        numSellers (int): Number of sellers in case the agents are generated. Default=0
    Internal variables:
        TODO: Finish the docstring!
    """

    def __init__(
        self,
        numDays: int = 1,
        agents: list[Agent] = None,
        defaultStrategy: int = WALKBY,
        numBuyers: int = 0,
        numSellers: int = 0,
    ) -> None:
        self.numDays = numDays

        if agents is None:
            self.agents = self.generateAgents(numBuyers, numSellers, defaultStrategy)
        else:
            self.agents = agents

        self.daysSimulated = 0
        self.days = []

    def generateAgents(
        self, numBuyers: int = 0, numSellers: int = 0, strategy: int = WALKBY
    ) -> list[Agent]:
        """Generate a given number of buyers and sellers. Returns a list of agents"""
        agents = []

        for _ in range(numBuyers):
            # TODO: review how to randomly generate price limits This is a mock up for the moment!
            priceLimit = random(50, 100)
            initialPrice = random(priceLimit, 100)

            agents.append(Agent(BUYER, strategy, priceLimit, initialPrice))

        for _ in range(numSellers):
            # TODO: review how to randomly generate price limits
            priceLimit = random(50, 100)
            initialPrice = random(priceLimit, 100)
            log.debu
            agents.append(Agent(SELLER, strategy, priceLimit, initialPrice))

        return agents

    def insertAgent(self, newAgent: Agent) -> None:
        """Insert a new agent to the list of agents of the simulation"""
        self.agents.append(newAgent)

    def simulate(self, days: int = None):
        """Execute the simulation for a given number of days"""
        if days is None:
            days = self.numDays

        for _ in range(days):
            currentDay = Day(self.agents)
            currentDay.execute()
            currentDay.getStats()
            self.daysSimulated += 1
            self.days.append(currentDay)


# TODO: Review!
"""groupBuyers = [Agent(BUYER, WALKBY, 9, 7)]
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
"""
