# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import os
import sys
import argparse
import subprocess

print("")
print("Python version = " + sys.version)
print("Driver arguments = " + repr(sys.argv))

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print("== Execution Output ==")
print("Square of {0} is {1}".format(sys.argv[-1],args.square**2))
