def get_iter_string(hex_string):
    hex_string = hex_string[2:]
    leading_zeros = 0
    for c in hex_string:
        if c == "0":
            leading_zeros += 1
        else:
            break

    if leading_zeros == 40:
        first_non_zero = None
    else:
        first_non_zero = int("0x" + hex_string[leading_zeros], 16)

    if first_non_zero is not None:
        iters = 16 ** (leading_zeros) * 16 ** ((0xF - first_non_zero) / 0xF)
    else:
        iters = 16 ** leading_zeros

    return iters


def diff_to_iter(hex_string):
    if hex_string == "NaN":
        return "NaN"
    
    iters = get_iter_string(hex_string)

    if iters < 1_000_000:
        return str(int(iters)) + "H /s"
    elif iters < 1_000_000_000:
        return f"{iters / 1_000_000:.2f} MH/s"
    elif iters < 1_000_000_000_000:
        return f"{iters / 1_000_000_000:.2f} GH/s"
    else:
        return f"{iters / 1_000_000_000_000:.2f} TH/s"


def get_disclaimer(difficulty_string):
    iter = get_iter_string(difficulty_string)

    if iter == "NaN":
        return "Could not calculate hashrate"
    elif iter < 1_000_000:
        return """Difficulty is VERY low, expect miner to find a solution in sub-second
Feel free to use nvidia-smi or analogue to check the GPU load"""
    elif iter < 1_000_000_000:
        return """Difficulty is QUITE low, expect miner to find a solution in one second on one RTX-4090
Feel free to use nvidia-smi or analogue to check the GPU load"""
    elif iter < 10_000_000_000:
        return """Difficulty is MEDIUM, expect miner to find a solution in 10 seconds on one RTX-4090
Feel free to use nvidia-smi or analogue to check the GPU load"""
    elif iter < 100_000_000_000:
        return """Difficulty is MODERATELY HIGH, expect miner to find a solution in 100 seconds on one RTX-4090
Time will scale linearly down with more GPUs
Feel free to use nvidia-smi or analogue to check the GPU load"""
    elif iter < 1_000_000_000_000:
        return """Difficulty is VERY HIGH, expect miner to find a solution in MORE than 100 seconds on one RTX-4090
Time will scale linearly down with more GPUs
and don't worry if you don't see submissions, you are on the uncharted territory of maximum GPU performace
Feel free to use nvidia-smi or analogue to check the GPU load"""
    else:
        return """Difficulty is EXTREMELY HIGH, expect miner to find a solution in MORE than 1000 seconds on one RTX-4090
Time will scale linearly down with more GPUs
and don't worry if you don't see submissions, you are on the uncharted territory of maximum GPU performace
Feel free to use nvidia-smi or analogue to check the GPU load"""


def print_strat_banner():
    print("""
Launching Infinity Miner.
If you haven't seen any warnings above this line -- it means you are good to go.
However, keep an eye for any warnings that might appear later in our journey.

Expect to see the [MINING STATS] giving you quick peak into the current state of the miner.
And 'New submission' logs with time and tx_hash, this means that miner found a new solution and submitted it.
          
IF you want to get more information about what's happening under the hood -- check debug logs.
""")
