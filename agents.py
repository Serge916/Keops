import random

# Agent type
SELLER = 0
BUYER = 1
BOTH = 2
# Agent strategy
WALKBY = 0
NEGOTIATE = 1


class Agent:
    """Creates a market agent

    Args:
        type (int): The type of the agent: BUYER/SELLER
        strategy (int): The strategy of the agent
        priceLimit (int): The max (buyer) or min (seller) price the agent is willing to acccept
        initialPrice (int): The initial value for currentPrice
    Internal variables:
        currentPrice (int): The price the agent asks for in the current iteration
        streak (int): The number of successful (positive) or failed (negative) days in a row
        attended (bool): True if the agent already participated in the current day, False otherwise
        success (bool): True if the agent successfully attended a meeting in the current day, False otherwise
    """

    def __init__(
        self, agentType, strategy=WALKBY, priceLimit=None, initialPrice=None
    ) -> None:
        self.type = agentType
        self.strategy = strategy
        self.priceLimit = priceLimit
        self.currentPrice = initialPrice
        print(f"Created agent of type {self.type}")

        self.streak = 0
        self.attended = False
        self.discarded = False
        self.success = False

    def reflection(self) -> None:
        """Agent reflects on the last round"""
        pass
