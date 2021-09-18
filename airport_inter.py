#!/usr/bin/env python3
import subprocess
import re
import os

# Interface with macOS airport util 

AIRPORT_PATH = [os.environ.get(
    'AIRPORT_PATH', 
    '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport')]

def main(args):
    process = subprocess.run(AIRPORT_PATH + args)

main(['-I'])
