import numpy as np
from random import random, randrange

from agents import *

log = logging.getLogger(__name__)


class AgentGenerator:
    def __init__(self) -> None:
        pass

    def generateAgentsGaussian(
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

    def generateAgentsBeta(
        numBuyers: int = 0, numSellers: int = 0, strategy: int = STUBBORN
    ) -> list[Agent]:
        """Generate a given number of buyers and sellers. Returns a list of agents"""
        agents = []

        log.debug(
            f"Generating {numBuyers} buyers and {numSellers} sellers with strategy {strategy}"
        )

        rndGenerator = np.random.default_rng()

        for _ in range(numBuyers):
            # TODO: review how to randomly generate price limits This is a mock up for the moment!
            initialPrice, priceLimit = np.sort(
                rndGenerator.beta(a=BETA_DIST_ALPHA, b=BETA_DIST_BETA, size=2)
                * (BETA_DIST_MAX_VAL - BETA_DIST_MIN_VAL)
                + BETA_DIST_MIN_VAL
            )
            agents.append(Agent(BUYER, strategy, priceLimit, initialPrice))

        for j in range(numSellers):
            # TODO: review how to randomly generate price limits
            priceLimit, initialPrice = np.sort(
                rndGenerator.beta(a=BETA_DIST_ALPHA, b=BETA_DIST_BETA, size=2)
                * (BETA_DIST_MAX_VAL - BETA_DIST_MIN_VAL)
                + BETA_DIST_MIN_VAL
            )
            agents.append(Agent(SELLER, strategy, priceLimit, initialPrice))

        return agents
