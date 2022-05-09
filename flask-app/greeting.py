#!/usr/bin/env python3
import sys

greeted = "world"

if sys.argv[1]:
    greeted = sys.argv[1]

sys.stdout.write("Hello {}!".format(greeted))