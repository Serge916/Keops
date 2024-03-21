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

    def __init__(self, agents: list[Agent], dayId: int, maxRounds: int = None) -> None:
        self.pendingAgents = agents
        self.completedAgents = []

        self.dayId = dayId
        self.maxRounds = maxRounds

        self.rounds = []

    def run(self):
        while not self.__dayEnded():
            # The day has not ended so we create a new round
            currentRound = Round(self.pendingAgents)

        pass

    def getStats(self):
        # TODO: How should we do this?
        pass

    def __dayEnded() -> bool:

        return True
