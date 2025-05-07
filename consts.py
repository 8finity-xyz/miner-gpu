"""
Chain specific paraeters,
better do not adjust them
we will update them on our github if there will be a need for it
"""

CHAIN_ID = 146
POW_CONTRACT = "0x8888FF459Da48e5c9883f893fc8653c8E55F8888"
INFINITY_ADDRESS = "0x888852d1c63c7b333efEb1c4C5C79E36ce918888"
POW_NEW_PROBLEM_TOPIC0 = (
    "0xa100d84256eafde4f67167e266005a7b734f135b1ba16dd349e2469a81d05c47"
)
PROBLEM_SELECTOR = "0x88f116d0"
BALANCE_OF_SELECTOR = "0x70a08231"
GAS_LIMIT_SUBMIT = 2_000_000

"""
    be creative, pick your own data, don't make it too long though,
    code will compulsory fail if len(SIGN_DATA) > 32, so keep that in mind
"""
SIGN_DATA = bytes.fromhex("deadbeef1337cafebabe")

"""
    [TX-BUILDER] feel free to tune it
    or build a script to tune it
"""
MAX_PRIORITY_FEE_MWEI = 500
BASE_FEE_K = 2

"""
    [MINER] Mining params section:
    feel free to tweak this parameters until it works the best for you
    original profanity2 params are mirrored here: https://github.com/1inch/profanity2

Tweaking:
    WORKSIZE_LOCAL      Set OpenCL local work size. [default = 64]
    WORKSIZE_MAX        Set OpenCL maximum work size. [default = -i * -I]
    INVERSE_SIZE        Set size of modular inverses to calculate in one work item. [default = 255]
    INVERSE_MULTIPLE    Set how many above work items will run in parallell. [default = 16384]

Note:
    My own strategy is modifying INVERSE_MULTIPLE while keeping other parameters default
    For Apple Silicon expect something like 1024 to be an optimal INVERSE_MULTIPLE size

    For NVIDIA GPU -- 16384 will be a great option

    Keep in mind that this number HAS TO BE a power of 2 (1024, 2048, 4096, etc)
"""
WORKSIZE_LOCAL = 64
WORKSIZE_MAX = 0  # 0 means default
INVERSE_SIZE = 255
INVERSE_MULTIPLE = 1024

"""
    Should program output anything in std::out ?
"""
PROFANITY2_VERBOSE_FLAG = False  # do you want profanity2 working logs?


"""
    500 ms polling loop step 
    15 min --> 720_000 steps
    session will be updated once in a hour
"""
SESSION_UPATE_STEPS = 1_800

"""
    5 ms main loop step 
    1 s --> 200 steps
"""
CLI_LOG_SECONDS_STEP = 10

DEFAULT_POLL_INTERVAL_SECONDS = 0.3  # 300 ms
DEFAULT_MAIN_LOOP_STEP_SECONDS = 0.005  # 5ms
