from constants import *


class Agent:
    """Creates a market agent
    ### Args:
        - type (int): The type of the agent: BUYER/SELLER
        - strategy (int): The strategy of the agent
        - priceLimit (float): The max (buyer) or min (seller) price the agent is willing to acccept
        - initialPrice (float): The initial value for goalPrice
    ### Internal variables:
        - goalPrice (float): The price the agent asks for in the current iteration
        - lastAgreedPrice (float): The price agreed by the agent in the last meeting
        - streak (int): The number of successful (positive) or failed (negative) days in a row
        - attended (bool): True if the agent already participated in the current day, False otherwise
        - success (bool): True if the agent successfully attended a meeting in the current day, False otherwise
    """

    def __init__(
        self,
        agentType: int,
        strategy: int = STUBBORN,
        priceLimit: float = None,
        initialPrice: float = None,
    ) -> None:
        if agentType == BUYER and initialPrice > priceLimit:
            raise ValueError(
                "Buyer cannot have an initial price higher than the price limit."
            )
        if agentType == SELLER and initialPrice < priceLimit:
            raise ValueError(
                "Seller cannot have an initial price lower than the price limit."
            )
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
        """Agent reflects on the last round, i.e. it changes the goal price accordingly."""
        # previousGoalPrice + streakMultiplier * (agreedPrice - previousGoalPrice)
        # TO DO: Deal with buyer negative streak. Is it even possible without being discarded?
        if not self.attended:
            return

        lastPoint = 1 if self.success == True else -1
        if lastPoint * self.streak > 0:
            self.streak = lastPoint * (abs(self.streak) + 1)
        else:
            self.streak = lastPoint

        if self.type == BUYER:
            goalPrice = (1 - ALPHA) * self.goalPrice + ALPHA * abs(self.streak) * (
                self.lastAgreedPrice - self.goalPrice
            )
            self.goalPrice = max(goalPrice, self.priceLimit)
        else:
            goalPrice = (1 - ALPHA) * self.goalPrice + ALPHA * abs(self.streak) * (
                self.lastAgreedPrice - self.goalPrice
            )
            self.goalPrice = min(goalPrice, self.priceLimit)

    def paramUpdate(
        self,
        priceLimit: float,
        currentPrice: float,
    ) -> None:
        """
        Update the prices of the Agent
        ### Args:
        - priceLimit (float): The max (buyer) or min (seller) price the agent is willing to acccept
        - initialPrice (float): The current value for goalPrice
        """
        self.priceLimit = priceLimit
        self.goalPrice = currentPrice
