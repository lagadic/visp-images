#!/usr/bin/env python3
#
# ViSP, open source Visual Servoing Platform software.
# Copyright (C) 2005 - 2025 by Inria. All rights reserved.
#
# This software is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# See the file LICENSE.txt at the root directory of this source
# distribution for additional information about the GNU GPL.
#
# For using ViSP with software that can not be combined with the GNU
# GPL, please contact Inria about acquiring a ViSP Professional
# Edition License.
#
# See https://visp.inria.fr for more information.
#
# This software was developed at:
# Inria Rennes - Bretagne Atlantique
# Campus Universitaire de Beaulieu
# 35042 Rennes Cedex
# France
#
# If you have questions regarding the use of this file, please contact
# Inria at visp@inria.fr
#
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#
# Description:
# Code to print NumPy NPZ data.

import argparse
import sys
import numpy as np

def main():
    print(f"Python version: {sys.version}")
    print(f"Version info: {sys.version_info}")
    print(f"NumPy info: {np.__version__}")

    parser = argparse.ArgumentParser(description='Read NPZ file using NumPy and dump its content.')
    parser.add_argument("-i", "--input", type=str, required=True, help="Input file")
    args = parser.parse_args()

    input_npz = args.input
    print(f"Load: {input_npz}")

    data_dict = np.load(input_npz)
    for key, value in data_dict.items():
        print(f"key: {key} ; value: {value} ; shape: {value.shape}")

if __name__ == '__main__':
    main()