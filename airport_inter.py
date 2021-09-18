#!/usr/bin/env python3
import subprocess
import re
import os
import time

# Interface with macOS airport util 

AIRPORT_PATH = [os.environ.get(
    'AIRPORT_PATH', 
    '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport')]

def gen_cmd(args):
    return AIRPORT_PATH + args 

def get_info(args):
    process = subprocess.Popen(gen_cmd(args), stdout=subprocess.PIPE)
    out, _ = process.communicate()
    process.wait()
    return out 

def split_lines(lines, start=0):
    return lines.split('\n')[start:]

def reformat_info_result(result):
    def reformat_info_result_line(line):
        _, value = line.split(':', 1)
        return value.strip()

    results_in_lines = filter(lambda line: line, split_lines(result))
    info_args = map(reformat_info_result_line, results_in_lines)
    return datatypes.InfoResult(*info_args)

def main():
    while True:
        a = (get_info(['-I']))
        print(reformat_info_result(a))
        time.sleep(1)


main()


