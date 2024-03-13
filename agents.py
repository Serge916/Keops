from constants import *


class Agent:
    """Creates a market agent

    Args:
        type (int): The type of the agent: BUYER/SELLER
        strategy (int): The strategy of the agent
        priceLimit (float): The max (buyer) or min (seller) price the agent is willing to acccept
        initialPrice (float): The initial value for goalPrice
    Internal variables:
        goalPrice (float): The price the agent asks for in the current iteration
        lastAgreedPrice (float): The price agreed by the agent in the last meeting
        streak (int): The number of successful (positive) or failed (negative) days in a row
        attended (bool): True if the agent already participated in the current day, False otherwise
        success (bool): True if the agent successfully attended a meeting in the current day, False otherwise
    """

    def __init__(
        self,
        agentType: int,
        strategy: int = WALKBY,
        priceLimit: float = None,
        initialPrice: float = None,
    ) -> None:
        self.type = agentType
        self.strategy = strategy
        self.priceLimit = priceLimit
        self.goalPrice = initialPrice
        self.lastAgreedPrice = 0
        self.streak = 0
        self.attended = False
        self.discarded = False
        self.success = False

    def reflection(self) -> None:
        """Agent reflects on the last round"""
        # previousGoalPrice + streakMultiplier * (agreedPrice - previousGoalPrice)
        # TO DO: Deal with buyer negative streak. Is it even possible without being discarded?
        goalPrice = (1 - ALPHA) * self.goalPrice + ALPHA * abs(self.streak) * (
            self.lastAgreedPrice - self.goalPrice
        )
        # Prices cannot go out of bounds
        self.goalPrice = (
            max(goalPrice, self.priceLimit)
            if self.type == BUYER
            else min(goalPrice, self.priceLimit)
        )
