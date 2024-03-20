from random import random, randrange
import logging
from datetime import datetime
import time

from agents import *
from day import *

log = logging.getLogger(__name__)
logging.basicConfig(
    filename="simulator.log",
    filemode="a",
    level=logging.DEBUG,
    format="[%(levelname)s] %(name)s-%(funcName)s(): %(message)s",
)


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
        log.debug(f"choden days: {numDays}")

        if agents is None:
            self.agents = self.generateAgents(numBuyers, numSellers, defaultStrategy)
        else:
            self.agents = agents

        self.daysSimulated = 0
        self.days = []
        self.simExecutionTime = 0

    def generateAgents(
        self, numBuyers: int = 0, numSellers: int = 0, strategy: int = WALKBY
    ) -> list[Agent]:
        """Generate a given number of buyers and sellers. Returns a list of agents"""
        agents = []

        for _ in range(numBuyers):
            # TODO: review how to randomly generate price limits This is a mock up for the moment!
            priceLimit = randrange(50, 100)
            initialPrice = randrange(priceLimit, 100)

            agents.append(Agent(BUYER, strategy, priceLimit, initialPrice))

        for _ in range(numSellers):
            # TODO: review how to randomly generate price limits
            priceLimit = randrange(50, 100)
            initialPrice = randrange(priceLimit, 100)
            agents.append(Agent(SELLER, strategy, priceLimit, initialPrice))

        return agents

    def insertAgent(self, newAgent: Agent) -> None:
        """Insert a new agent to the list of agents of the simulation"""
        self.agents.append(newAgent)

    def simulate(self, days: int = None):
        """Execute the simulation for a given number of days"""
        t0 = time.time()
        if days is None:
            days = self.numDays

        for _ in range(days):
            currentDay = Day(self.agents)
            currentDay.execute()
            currentDay.getStats()
            self.daysSimulated += 1
            self.days.append(currentDay)

        # End of the simulation. Get the timestamp to added the simulation time to the class
        t1 = time.time()
        self.simExecutionTime += t0 - t1


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

if __name__ == "__main__":
    log.info(
        f"""/****************** Starting a brand new simulation! ******************
                            |
                            |            Date of execution: {datetime.now()}                            
                            |                      
                            \\**********************************************************************

"""
    )
    sim = MarketSimulator(numDays=10, defaultStrategy=WALKBY, numBuyers=1, numSellers=1)
    log.info(
        f"""/************************ End of simulation! ************************
                            |
                            |              Execution time: {sim.simExecutionTime}
                            |
                            \\**********************************************************************

"""
    )
