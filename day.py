import logging

from agents import *
from round import *

log = logging.getLogger(__name__)


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
        log.debug(
            f"Creating class Day with the following arguments dayId: {dayId}, numAgents: {len(agents)}, maxRounds: {maxRounds}"
        )
        self.pendingAgents = agents
        self.agents = agents

        self.dayId = dayId
        self.maxRounds = maxRounds

        self.__run()

    def getStats(self) -> None:
        # TODO: How should we do this?

        pass

    def __run(self) -> None:
        log.info(
            f"//////////////////////////DAWN OF DAY: {self.dayId}\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"
        )
        roundCount = 0
        numMeetings = 1
        while self.pendingAgents and roundCount < self.maxRounds and numMeetings != 0:
            log.debug(f"Iteration Round: {roundCount}. Maximum of {self.maxRounds}")
            # The day has not ended so we create a new round
            currentRound = Round(self.pendingAgents, roundCount, RANDOM)

            numMeetings = currentRound.numMeetings

            self.pendingAgents = [
                agent for agent in self.pendingAgents if not agent.success
            ]
            roundCount += 1

            log.info(f"Number of remaining pending agnets: {len(self.pendingAgents)}")
            log.info(f"Num meetings taken place in last round: {numMeetings}")

        log.debug(
            f"No more rounds after round {roundCount}. Remaning pending agents: {len(self.pendingAgents)}. Num meetings last round {numMeetings}"
        )
        log.debug(f"The rounds of the day finished, starting reflection of all agents")
        for agent in self.agents:
            agent.reflection()

        log.info(
            f"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\END OF DAY: {self.dayId}//////////////////////////\n"
        )
