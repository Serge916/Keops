import logging
from datetime import datetime

from market import *

log = logging.getLogger(__name__)
statsFolder = "output/"

logging.basicConfig(
    filename="simulator.log",
    filemode="a",
    level=logging.DEBUG,
    format="[%(levelname)s] %(name)s-%(funcName)s(): %(message)s",
)

if __name__ == "__main__":
    log.info(START_MSG.format(datetime.now()))

    sim = MarketSimulator(
        numDays=30, defaultStrategy=NEGOTIATE, numBuyers=3, numSellers=4
    )

    sim.simulate()

    log.info(END_MSG.format(sim.simExecutionTime))
    Agent.classStatsDf.to_pickle(f"{statsFolder}agent.pkl")
    Meeting.classStatsDf.to_pickle(f"{statsFolder}meeting.pkl")
    Round.classStatsDf.to_pickle(f"{statsFolder}round.pkl")
