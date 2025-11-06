/*
 * ViSP, open source Visual Servoing Platform software.
 * Copyright (C) 2005 - 2025 by Inria. All rights reserved.
 *
 * This software is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * See the file LICENSE.txt at the root directory of this source
 * distribution for additional information about the GNU GPL.
 *
 * For using ViSP with software that can not be combined with the GNU
 * GPL, please contact Inria about acquiring a ViSP Professional
 * Edition License.
 *
 * See https://visp.inria.fr for more information.
 *
 * This software was developed at:
 * Inria Rennes - Bretagne Atlantique
 * Campus Universitaire de Beaulieu
 * 35042 Rennes Cedex
 * France
 *
 * If you have questions regarding the use of this file, please contact
 * Inria at visp@inria.fr
 *
 * This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
 * WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
 *
 * Description:
 * Code to generate reference NPZ files for CI tests using the ViSP cnpy lib.
 */

#include <visp3/core/vpConfig.h>
#include <visp3/core/vpIoTools.h>

namespace
{
bool BigEndianTest()
{
  int x = 1;
  return !((reinterpret_cast<char *>(&x))[0]);
}

bool BigEndianTest2()
{
  static_assert(sizeof(uint32_t) == 4);
  union {
    uint32_t i;
    char c[4];
  } constexpr test = {0x01020304};

  return !(test.c[0] == 0x04);
}
}

int main(int , char *[])
{
  // This code is used to generate NPZ files for ViSP test data.
  // Run this on the CI for little and big endian data.

  std::cout << "BigEndianTest()=" << BigEndianTest() << std::endl;
  std::cout << "BigEndianTest2()=" << BigEndianTest2() << std::endl;

  // Save multiple types
  std::string npz_filename = "visp_npz_test_data_cnpy.npz";
  const std::string bool_false_identifier = "My bool false data";
  const std::string bool_true_identifier = "My bool true data";
  const std::string uint32_identifier = "My uint32 data";
  const std::string int64_identifier = "My int64 data";
  const std::string float_identifier = "My float data";
  const std::string double_identifier = "My double data";
  const std::string complex_identifier = "My complex data";
  const std::string matrix_int_identifier = "My int matrix data";
  const std::string matrix_flt_identifier = "My float matrix data";
  const std::string vec_complex_identifier = "My complex vector data";
  {
    /* Simple types */
    bool b_false = false;
    visp::cnpy::npz_save(npz_filename, bool_false_identifier, &b_false, { 1 }, "w");

    bool b_true = true;
    visp::cnpy::npz_save(npz_filename, bool_true_identifier, &b_true, { 1 }, "a");

    uint32_t uint32_data = 99;
    std::cout << "Save uint32 data: " << uint32_data << std::endl;
    visp::cnpy::npz_save(npz_filename, uint32_identifier, &uint32_data, { 1 }, "a");

    int64_t int64_data = -123456;
    std::cout << "Save int64 data: " << int64_data << std::endl;
    visp::cnpy::npz_save(npz_filename, int64_identifier, &int64_data, { 1 }, "a");

    float float_data = -456.51f;
    std::cout << "Save float data: " << float_data << std::endl;
    visp::cnpy::npz_save(npz_filename, float_identifier, &float_data, { 1 }, "a");

    double double_data = 3.14;
    std::cout << "Save double data: " << double_data << std::endl;
    visp::cnpy::npz_save(npz_filename, double_identifier, &double_data, { 1 }, "a");

    std::complex<double> complex_data(float_data, double_data);
    std::cout << "Save complex data: real=" << complex_data.real() << " ; imag=" << complex_data.imag() << std::endl;
    visp::cnpy::npz_save(npz_filename, complex_identifier, &complex_data, { 1 }, "a");

    /* 3D mat types */
    size_t height = 5, width = 7, channels = 3;
    std::vector<int> save_vec_int;
    std::vector<float> save_vec_flt;
    save_vec_flt.reserve(height*width*channels);
    for (int i = 0; i < static_cast<int>(height*width*channels); ++i) {
      save_vec_int.push_back(i);
      save_vec_flt.push_back(i);
    }

    visp::cnpy::npz_save(npz_filename, matrix_int_identifier, &save_vec_int[0], { height, width, channels }, "a");
    visp::cnpy::npz_save(npz_filename, matrix_flt_identifier, &save_vec_flt[0], { height, width, channels }, "a");

    /* Vector of complex<double> */
    std::vector<std::complex<float>> vec_complex_data;
    for (int i = 0; i < 3; i++) {
      vec_complex_data.push_back(std::complex<float>(complex_data.real()*(i+1), complex_data.imag()*2*(i+1)));
    }
    visp::cnpy::npz_save(npz_filename, vec_complex_identifier, &vec_complex_data[0], { vec_complex_data.size() }, "a");
  }

  {
    visp::cnpy::npz_t npz_data = visp::cnpy::npz_load(npz_filename);

    std::cout << npz_filename << " file contains the following data:" << std::endl;
    for (visp::cnpy::npz_t::const_iterator it = npz_data.begin(); it != npz_data.end(); ++it) {
      std::cout << "  " << it->first << std::endl;
    }
    std::cout << std::endl;

    visp::cnpy::npz_t::iterator it_bool_false = npz_data.find(bool_false_identifier);
    visp::cnpy::npz_t::iterator it_bool_true = npz_data.find(bool_true_identifier);
    std::cout << "it_bool_false=" << *(it_bool_false->second.data<bool>()) << std::endl;
    std::cout << "it_bool_true=" << *(it_bool_true->second.data<bool>()) << std::endl;
  }

  return EXIT_SUCCESS;
}
