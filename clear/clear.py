# Milosz Jura milessic 2023

import os


def clear():
    r"""clears console based on user OS"""
    os.system('cls' if os.name == 'nt' else 'clear')
