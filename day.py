from agents import *
from round import *


class Day:
    # TODO: Work on day!
    def __init__(self, agents: list[Agent], dayId: int):
        self.agents = agents
        self.dayId = dayId
        self.inactiveAgents = []

    def run(self):
        # TODO: implement run
        for day in range(self.dayId):
            activeAgents = [agent for agent in self.agents if not agent.discarded]
            concurringAgents = [agent for agent in activeAgents if not agent.success]
            runRound(
                [agent for agent in concurringAgents if agent.type == BUYER],
                [agent for agent in concurringAgents if agent.type == SELLER],
            )

    def getStats(self):
        pass
