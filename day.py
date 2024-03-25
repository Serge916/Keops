from agents import *
from round import *


class Day:
    # TODO: Work on day!
    def __init__(self, agents: list[Agent], dayId: int):
        self.agents = agents
        self.dayId = dayId

    def run(self):
        # TODO: implement run
        for day in range(self.dayId):
            print(f"It's a new day!. Iteration {day}")
            activeAgents = [agent for agent in self.agents if not agent.discarded]
            roundNum = 0
            concurringBuyers = [
                agent
                for agent in activeAgents
                if not agent.success and agent.type == BUYER
            ]
            concurringSellers = [
                agent
                for agent in activeAgents
                if not agent.success and agent.type == SELLER
            ]
            while roundNum < MAX_ROUND and concurringSellers and concurringBuyers:
                Round(
                    buyers=concurringBuyers,
                    sellers=concurringSellers,
                    matchingStrategy=RANDOM,
                )
                roundNum += 1

    def getStats(self):
        pass
