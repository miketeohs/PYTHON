#!/usr/bin/python3
# pw.py - An insecure password locker program.
#
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--firstName', type=str, required=True)
args = parser.parse_args()
print('Hello,', args.firstName)
