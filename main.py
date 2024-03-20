import logging
from datetime import datetime

from market import *

log = logging.getLogger(__name__)

logging.basicConfig(
    filename="simulator.log",
    filemode="a",
    level=logging.DEBUG,
    format="[%(levelname)s] %(name)s-%(funcName)s(): %(message)s",
)

if __name__ == "__main__":
    log.info(START_MSG.format(datetime.now()))

    sim = MarketSimulator(numDays=10, defaultStrategy=WALKBY, numBuyers=1, numSellers=1)

    log.info(END_MSG.format(sim.simExecutionTime))
