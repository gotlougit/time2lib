#!/usr/bin/env python3

import time

def wait(hr,mn):
    try:
        hr = int(hr)
        mn = int(mn)
    except ValueError:
        print("Wrong values have been entered!")
        quit()

    t = (hr * 3600) + (mn * 60)
    time.sleep(t)
    return "timeup"
