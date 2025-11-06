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
# Code to generate reference NPZ files for CI tests using the NumPy lib.

import argparse
import sys
import numpy as np

def main():
    print(f"Python version: {sys.version}")
    print(f"Version info: {sys.version_info}")
    print(f"NumPy info: {np.__version__}")

    npz_filename = "visp_npz_test_data_numpy.npz"

    bool_false_identifier = "My bool false data"
    bool_true_identifier = "My bool true data"
    uint32_identifier = "My uint32 data"
    int64_identifier = "My int64 data"
    float_identifier = "My float data"
    double_identifier = "My double data"
    matrix_int_identifier = "My int matrix data"
    matrix_flt_identifier = "My float matrix data"

    data_dict = dict()
    data_dict[bool_false_identifier] = False
    data_dict[bool_true_identifier] = True
    data_dict[uint32_identifier] = np.uint32(99)
    data_dict[int64_identifier] = np.int64(-123456)
    data_dict[float_identifier] = np.float32(-456.51)
    data_dict[double_identifier] = np.float64(3.14)

    height, width, channels = 5, 7, 3
    total = height*width*channels
    vec_int = np.empty((height, width, channels), dtype=np.int32)
    vec_flt = np.empty((height, width, channels), dtype=np.float32)
    for i in range(height):
        for j in range(width):
            for k in range(channels):
                vec_int[i, j, k] = i*width*channels + j*channels + k
                vec_flt[i, j, k] = i*width*channels + j*channels + k

    data_dict[matrix_int_identifier] = vec_int
    data_dict[matrix_flt_identifier] = vec_flt
    np.savez(npz_filename, **data_dict)

if __name__ == '__main__':
    main()