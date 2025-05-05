# Infinity GPU Miner

A **heavily optimized** OpenCL miner for solving the [Infinity Token](https://github.com/8finity-xyz/protocol) Proof-of-Work **Magic XOR** problem.  

> **Acknowledgment**  
> This miner is based on the [profanity2](https://github.com/1inch/profanity2) approach, with special modifications to handle Infinity’s `MagicXOR` puzzle. Many thanks to the original profanity2 developers for the incredible optimizations.

---

## 1. Installation

<details>
    <summary>Dependencies & Platforms & Notes</summary>

This miner is a heavily optimized software, hence it is quite picky dependencies-wise. Please make sure you have all the necessary dependancies installed and working together.

**An optimal option for most of the users will be to proceed with Docker build on a server with NVIDIA GPU.**

- **OpenCL** (SDK + GPU drivers)  
  - Linux: `ocl-icd-opencl-dev`, `libopencl-clang-dev`, compatible NVIDIA or AMD drivers
  - macOS: OpenCL must be available; Apple Silicon with GPU drivers (Metal/OpenCL bridging) tested.
- **C++11** compiler (e.g., `g++`).
- **Python 3.10+** with `pybind11`, `safe-pysha3`, `ecdsa`, `coincurve`, `web3`, `websockets`, etc.
- **Make** (for building `magicXorMiner.so`).
- (Optional) **Docker** (for container builds).

> **Tested** primarily on Linux (NVIDIA GPUs) and Apple Silicon. Other platforms *may* work but are not guaranteed.

</details>


### 1.1 Linux Build

#### 1. **Recommended:** Build with Docker, using the provided Dockerfile:
```bash
    # build
    docker build -t infinity-miner .
    
    # Then run with GPU passthrough (e.g. NVIDIA Docker setup):
    docker run --gpus all -it infinity-miner /bin/bash

    # all repository files will be already there
    cd /app

    # test that OpenCL is indeed working under the hood
    python3 test_opencl_kernel.py 

    # Fill your miner address details & rpc details
    nano .env.example 

    # Move it to the .env
    mv .env.example .env

    # mine (but please do some setup first)
    python3 mine_infinity.py
 ```

Inside the container you’ll find the compiled `magicXorMiner.so` in /app.

#### 2. **Simplest Possible:** Pull prebuilt container from Docker Hub:
```bash
    docker pull otonashilabs/infinity-miner:latest
```
Then run:
```bash
    docker run --gpus all -it otonashilabs/infinity-miner:latest /bin/bash

    cd /app

    # test that OpenCL is indeed working under the hood
    python3 test_opencl_kernel.py 

    # Fill your miner address details & rpc details
    nano .env.example 

    # Move it to the .env
    mv .env.example .env
    
    # mine (but please do some setup first)
    python3 mine_infinity.py

```
The container already includes everything needed.

**NOTE: Ensure your Docker runtime and driver stack are set up to allow GPU access.**

#### 3. **Hardcore:** Bare-metal installation:
<details>
    <summary>Hardcore version</summary>

```bash
   # Install dependencies, for example on Ubuntu:
   sudo apt-get update && sudo apt-get install -y \
    g++ make git ocl-icd-opencl-dev libopencl-clang-dev curl python3 python3-pip clinfo nano

    # Install Python packages for Python
   pip3 install pybind11 safe-pysha3 ecdsa web3 coincurve websocket-client websockets dotenv 

   # Clone and build:
   git clone https://github.com/8finity-xyz/miner-gpu.git
   cd miner-gpu
   make clean && make

   # Potentially you might wanna use this line. If Nvidia and OpenCL aren't befrending
   # Configure OpenCL ICD for NVIDIA
   # mkdir -p /etc/OpenCL/vendors && echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd

   # test that OpenCL is indeed working under the hood
   python3 test_opencl_kernel.py 

    # Fill your miner address details & rpc details
    nano .env.example 

    # Move it to the .env
    mv .env.example .env

   # mine (but please do some setup first and congrats if this option succeded 🎉)
   python3 mine_infinity.py
```

This will produce `magicXorMiner.so`, with quite high probability.

However, there might be platform specific issues.  If experiencing any trouble with installing all of the dependancies -- please consider Docker build. 

**THIS IS THE HARDCORE BUILD VERSION**

</details>


### 1.2 macOS Build

macOS support is tested primarily on Apple Silicon (M1/M2). Adjust paths and frameworks for your environment.

<details>
    <summary>Mac OS OpenCL support</summary>

Installing OpenCL on a Mac with an Apple Silicon chip is a little different because Apple has deprecated OpenCL in favor of Metal. But OpenCL is still available on macOS, including on Apple Silicon (M1/M2/M3), just not actively developed

✅ 1. Xcode Command Line Tools (includes OpenCL)

Most macOS systems already have OpenCL support via system frameworks. All you really need is:
```bash
    xcode-select --install
```
This installs the command line developer tools, which include OpenCL headers and libraries in the system frameworks.

✅ 2. Check for OpenCL Framework

You can verify it’s available here:
```bash
    /System/Library/Frameworks/OpenCL.framework
```

Also:
```bash
    brew install clinfo
    clinfo
```

This will show you your OpenCL device stats. If it's working - you are good to go

</details>

To build:
```bash
    # install dependancies (uncomment on need) ideally install only the things that you need
    # brew install g++ make git curl python3 python3-pip clinfo nano

    # Install Python packages for Python (uncomment on need)
    # pip3 install pybind11 safe-pysha3 ecdsa web3 coincurve websocket-client websockets dotenv 

    git clone https://github.com/8finity-xyz/miner-gpu.git
    cd miner-gpu
    chmod +x build_mac.sh
    ./build_mac.sh

    # pay attention to any possible Error messages, ideally you will NOT get any
    # warning messages are OKAY

    # test that OpenCL is indeed working under the hood and that the build is succesefull
    python3 test_opencl_kernel.py 

    # Fill your miner address details & rpc details
    nano .env.example 

    # Move it to the .env
    mv .env.example .env
    
    # mine (but please do some setup first)
    python3 mine_infinity.py
```

**NOTE: This is the only way to launch miner on MacOs. Docker build DOES NOT work on Mac Os.**

---

## 2. Usage

In order to use this miner you will need to provide it with your mining wallet, and sonic blockchain connection details.

In order to do that - Let's take a closer look at env.example

```bash
# .env

# Valuables!
MASTER_ADDRESS = <PASTE_YOUR_ADDRESS_HERE>
MASTER_PKEY = <PASTE_YOUR_PRIVATE_KEY_HERE>
REWARDS_RECIPIENT_ADDRESS = <PASTE_YOUR_ADDREDD_HERE>


# RPCs
# if you dont know what is it - just leave it this way
INFINITY_RPC = https://rpc.blaze.soniclabs.com
INFINITY_WS = wss://rpc.blaze.soniclabs.com

```
Alright, in order to mine you need to have **mining wallet** with sonic balance there in order to cover gas expenses. 
We would reccomend you to use a separate wallet for mining. Ideally - create new wallet, top up it with some Sonic tokens and use it for mining. 

For secutiry purposes we have added an option to add a distinct **rewards wallet** - it is the wallet that will receive mining rewards in a form of Infinity tokens. This could be you any wallet, just make sure that you have an access to it. You can use **mining wallet** address in order to receive rewards, as you wish. But keep in mind that you can use other wallet as well!


So, in recap:
`MASTER_ADDRESS` is an address of your **mining wallet**
`MASTER_PKEY` is a private key of your **mining wallet** (you can export it from Metamask / Zerion)
`REWARDS_RECIPIENT_ADDRESS` is an addredd of your **rewards wallet**

Now, rpc's. If you have something like Alchemy / Infura - just take their connection URL for both `https` and `ws` and paste them. If you don't have them - no worries! You can use default connection links.


Security Warning
**This code is not designed with heavy security in mind; it’s best practice to use a dedicated wallet for mining with minimal funds.**

---

## 3. Tweaking / Advanced

<details>
    <summary>Tweaking</summary>

Within `config.py`, you’ll find the following configuration options:

Feel free to tune them! But make sure you know what you are doing.

```python
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
MINER_VERBOSE_FLAG = True # don't toggle these both to True -- they will mix, one at a time please


"""
    500 ms polling loop step 
    15 min --> 720_000 steps
    POLLING session will be updated once every 15 min
"""
SESSION_UPATE_STEPS = 1_800 

"""
    5 ms main loop step 
    1 s --> 200 steps
    Comand Line stats will be updated once every 500ms
"""
REFRESH_CLI_RATE = 100

DEFAULT_POLL_INTERVAL_SECONDS = 0.3 # 300 ms
DEFAULT_MAIN_LOOP_STEP_SECONDS = 0.005 # 5ms

```
</details>

---

## 4. License & Credits

**This software has been created by Otonashi Labs**

License & Credits
- This tool is adapted from 1inch/profanity2, all related disclaimers apply.
- No warranties. Use responsibly. Infinity GPU Miner authors are not liable for any damages or losses.

Enjoy mining Infinity — and if you discover improvements or have questions, feel free to open an issue or a pull request.
