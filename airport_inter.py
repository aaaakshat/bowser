#!/usr/bin/env python3
import subprocess
import re
import os
import time

# Interface with macOS airport util

AIRPORT_PATH = [os.environ.get(
    'AIRPORT_PATH',
    '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport')]


def call_cmd(*args):
    process = subprocess.Popen(
        args, stdout=subprocess.PIPE)
    out, _ = process.communicate()
    process.wait()
    return out

def build_airport_cmd(params):
    return AIRPORT_PATH + params

c = build_airport_cmd(params=['-I'])
print(call_cmd(*c))
