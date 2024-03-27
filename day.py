from agents import *
from round import *


class Day:
    """Class that manages the whole simulation

    Args:
        agents (list[Agent]): Array of agents that will take part on the day.
        dayId (int): Number to identify the day.
        maxRound (int): Maximum number of round a day might have.

    Internal variables:
        pendingAgents (list[Agent]): Array stating all the agents that have not made a succesful interaction yet
        completedAgents (list[Agent]): Array with all the agents that have already been succesful on the day
        dayId (int): Number to identify the day
        rounds (list[Round]): Array with the round happening on this day

    """

    def __init__(
        self, agents: list[Agent], dayId: int, maxRounds: int = MAX_ROUND_DEFAULT
    ) -> None:
        self.pendingAgents = agents
        self.agents = agents

        self.dayId = dayId
        self.maxRounds = maxRounds

        self.rounds = []

    def run(self) -> None:
        roundCount = 0
        while not self.__dayEnded(roundCount):
            # The day has not ended so we create a new round
            currentRound = Round(self.pendingAgents, RANDOM, roundCount)

            self.pendingAgents = [
                agent for agent in self.pendingAgents if not agent.success
            ]
            roundCount += 1

        for agent in self.agents:
            agent.reflection()

    def getStats(self) -> None:
        # TODO: How should we do this?

        pass

    def __dayEnded(self, roundCount) -> bool:
        if self.pendingAgents and roundCount < self.maxRounds:
            return False
        else:
            return True
