# Test data for visp::cnpy code

## Folder: numpy

It contains:
- `numpy_npz.py` --> the Python script to generate regression data for `modules/core/test/tools/io/catchNPZ.cpp`
- `visp_npz_test_data_numpy_LE.npz` --> data generated on a little-endian runner using the GitHub CI with:
  - `Python version: 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0]`
  - `NumPy info: 1.26.4`
- `visp_npz_test_data_numpy_BE.npz` --> data generated on a big-endian runner using the GitHub CI with:
  - `uraimo/run-on-arch-action@v3`
  - `Python version: 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0]`
  - `NumPy info: 1.26.4`

## Folder: visp_cnpy

Same thing with `generate_visp_npz_cnpy_ref.cpp` code to generate the reference data for the ViSP cnpy code.

## Hex dump

To easily view the content of a file in hexadecimal form:
- `hexdump -C -v the_desired_file.npz`

This is one way to retrieve the content of a file from a GitHub runner, at least the simplest solution I have found.
To convert from a textual binary representation to a binary file:
- `xxd -r -p the_desired_file.txt the_desired_file.npz` with `the_desired_file.txt` formatted such as having only the binary data (no memory address, no char visualisation)
