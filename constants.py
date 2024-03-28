# Agent type
SELLER = 0
BUYER = 1
BOTH = 2
# Agent strategy
STUBBORN = 0
NEGOTIATE = 1
# Matching strategy
RANDOM = 0
CHEAPEST_SELLERS_FIRST = 1
# Iteration constants
MAX_ROUND_DEFAULT = 10
# Exponential smoothing
ALPHA = 0.02


# Logger Strings
START_MSG = """/****************** Starting a brand new simulation! ******************
                            |
                            |            Date of execution: {0}                           
                            |                      
                            \\**********************************************************************

"""

END_MSG = """/************************ End of simulation! ************************
                            |
                            |              Execution time: {0}
                            |
                            \\**********************************************************************

"""
# Simulation parameters
DAYS = 3
BETA_DIST_MAX_VAL = 100
BETA_DIST_MIN_VAL = 30
BETA_DIST_ALPHA = 0.2
BETA_DIST_BETA = 0.4
