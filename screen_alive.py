import time
import pyautogui

pyautogui.FAILSAFE = False

__version__ = "0.0.1"


def shifting(seconds=60, verbose=False):
    while True:
        pyautogui.press("shift")
        if verbose:
            print(f"shifting version: {__version__}")
        time.sleep(seconds)


if __name__ == "__main__":
    shifting(verbose=True)
