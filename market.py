from random import random

from agents import *
from day import *


# Simulation parameters
DAYS = 3


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
        defaultStrategy: int = STUBBORN,
        numBuyers: int = 0,
        numSellers: int = 0,
    ) -> None:
        self.numDays = numDays

        if agents is None:
            self.agents = self.generateAgents(numBuyers, numSellers, defaultStrategy)
        else:
            self.agents = agents

    def generateAgents(numBuyers: int, numSellers: int, strategy: int) -> list[Agent]:
        """Function to generate a given number of buyers and sellers. Returns a list of agents"""
        agents = []

        for _ in range(numBuyers):
            # TODO: review how to randomly generate price limits
            priceLimit = random(50, 100)
            initialPrice = random(priceLimit, 100)

            agents.append(Agent(BUYER, strategy, priceLimit, initialPrice))

        for _ in range(numSellers):
            # TODO: review how to randomly generate price limits
            priceLimit = random(50, 100)
            initialPrice = random(priceLimit, 100)

            agents.append(Agent(SELLER, strategy, priceLimit, initialPrice))


# TODO: Review!
groupBuyers = [Agent(BUYER, STUBBORN, 9, 7)]
groupSellers = [Agent(SELLER, STUBBORN, 6, 6)]

for day in range(DAYS):
    for round in range(min(len(groupBuyers), len(groupSellers))):
        buyer = random.choice(groupBuyers)
        while buyer.attended == True:
            buyer = random.choice(groupBuyers)

        seller = random.choice(groupSellers)
        while seller.attended == True:
            seller = random.choice(groupSellers)

        runDay(buyer, seller)
