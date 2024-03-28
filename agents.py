import logging
import numpy as np
import pandas as pd
import pickle4 as pickle

from constants import *

log = logging.getLogger(__name__)

class Agent:
    classIdCounter = 0
    classStatsDf = pd.DataFrame()
    classStatsDf["day"] = pd.Series(dtype=int)
    classStatsDf["agentID"] = pd.Series(dtype=str)
    classStatsDf["agentType"] = pd.Series(dtype=int)
    classStatsDf["goalPrice"] = pd.Series(dtype=float)
    classStatsDf["strategy"] = pd.Series(dtype=int)
    classStatsDf["priceLimit"] = pd.Series(dtype=float)
    classStatsDf["streak"] = pd.Series(dtype=int)
    classStatsDf["discarded"] = pd.Series(dtype=bool)

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
        - discarded (bool): True if the agent is not active anymore
    """

    def __init__(
        self,
        agentType: int,
        strategy: int = STUBBORN,
        priceLimit: float = None,
        initialPrice: float = None,
        day: int = 0
    ) -> None:
        if agentType == BUYER and initialPrice > priceLimit:
            raise ValueError(
                "Buyer cannot have an initial price higher than the price limit."
            )
        if agentType == SELLER and initialPrice < priceLimit:
            raise ValueError(
                "Seller cannot have an initial price lower than the price limit."
            )
        self.agentID = f"{"S" if agentType == SELLER else "B"}{Agent.classIdCounter}"
        Agent.classIdCounter += 1

        self.type = agentType
        self.strategy = strategy
        self.priceLimit = priceLimit
        self.goalPrice = initialPrice
        self.lastAgreedPrice = 0
        self.streak = 0
        self.attended = False
        self.discarded = False
        self.success = False

        log.info(f"Created Agent ({self.agentID}) with Price Limit {self.priceLimit} and Goal Price {self.goalPrice}")
        self.getStats(day)

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
            goalPrice = self.goalPrice + ALPHA * self.streak * (
                self.lastAgreedPrice - self.goalPrice
            )
            self.goalPrice = min(goalPrice, self.priceLimit)
        else:
            goalPrice = self.goalPrice + ALPHA * abs(self.streak) * (
                self.lastAgreedPrice - self.goalPrice
            )
            self.goalPrice = max(goalPrice, self.priceLimit)

        self.success = False
        log.info(f"Agent ({self.agentID}) reflected on the last round, current Goal Price {self.goalPrice}")

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
        
        log.info(f"Agent ({self.agentID}) had its parameters externally modified, current Price Limit {self.priceLimit} and Goal Price {self.goalPrice}")

    def getStats(self, day):
        df = pd.DataFrame([{"day":day, "agentID":self.agentID, "agentType":self.type, "goalPrice":self.goalPrice, "strategy":self.strategy, "priceLimit":self.priceLimit, "streak":self.streak, "discarded":self.discarded}])
        Agent.classStatsDf = pd.concat([Agent.classStatsDf, df], ignore_index=True)
