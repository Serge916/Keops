import logging
from random import random, randrange
import time
import pickle4 as pickle

from agents import *
from day import *

log = logging.getLogger(__name__)


class MarketSimulator:
    """Class that manages the whole simulation

    ### Args:
        - numDays (int): Number of days to run the simulation for. Default=1
        - agents (list[Agent]): Array of agents that participate in the market. Default=None
        - defaultStrategy (int): If no agents are provided, then they will be generated with this defaultStrategy. Default=None
        - numBuyers (int): Number of buyers in case the agents are generated. Default=0
        - numSellers (int): Number of sellers in case the agents are generated. Default=0
    ### Internal variables:
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
        numAgents = len(agents) if agents is not None else numBuyers + numSellers
        log.debug(
            f"Creating class MarketSimulator with the following arguments numdays: {numDays}, numAgents: {numAgents}, defaultStrategy: {defaultStrategy}, numBuyers: {numBuyers}, numSellers: {numSellers}"
        )

        self.numDays = numDays

        if agents is None:
            log.debug("No agents provided so creating new ones.")
            self.agents = generateAgents(numBuyers, numSellers, defaultStrategy)
        else:
            self.agents = agents

        log.debug("Reseted internal variables of MarketSimulator")
        self.daysSimulated = 0
        self.days = []
        self.simExecutionTime = 0

    def insertAgent(self, newAgent: Agent) -> None:
        """Insert a new agent to the list of agents of the simulation"""
        log.debug("Added agent to the list of agents of the simulation")
        self.agents.append(newAgent)

    def simulate(self, days: int = None):
        """Execute the simulation for a given number of days"""
        t0 = time.time()
        if days is None:
            days = self.numDays

        log.info(
            f"Starting a simulation of {days} days. Which will generate the days from {self.daysSimulated+1} to {self.daysSimulated+days}"
        )

        for iteratedDay in range(days):
            log.debug(
                f"Iteration Day: {iteratedDay}. Global day is: {self.daysSimulated+1}"
            )
            currentDay = Day(self.agents, self.daysSimulated + 1)

            log.debug("End of day, obtaining stats and appending the day")
            currentDay.getStats()
            self.daysSimulated += 1
            self.days.append(currentDay)

        # End of the simulation. Get the timestamp to added the simulation time to the class
        t1 = time.time()
        self.simExecutionTime += t1 - t0


def generateAgents(
    numBuyers: int = 0, numSellers: int = 0, strategy: int = STUBBORN
) -> list[Agent]:
    """Generate a given number of buyers and sellers. Returns a list of agents"""
    agents = []

    log.debug(
        f"Generating {numBuyers} buyers and {numSellers} sellers with strategy {strategy}"
    )

    for _ in range(numBuyers):
        # TODO: review how to randomly generate price limits This is a mock up for the moment!
        priceLimit = randrange(50, 100)
        try:
            initialPrice = randrange(50, priceLimit)
        except ValueError:
            initialPrice = priceLimit
        agents.append(Agent(BUYER, strategy, priceLimit, initialPrice))

    for j in range(numSellers):
        # TODO: review how to randomly generate price limits
        priceLimit = randrange(50, 100)
        try:
            initialPrice = randrange(priceLimit, 100)
        except ValueError:
            initialPrice = priceLimit
        agents.append(Agent(SELLER, strategy, priceLimit, initialPrice))

    return agents
