# ViSP-images

ViSP-images contains data useful to run [ViSP][1] examples.

## Getting ViSP-images

To get the data set using git:

	git clone https://github.com/lagadic/ViSP-images.git
		
## Setting ViSP-images

To use the data set you have to set VISP_INPUT_IMAGE_PATH environment variable:

- on unix-like platforms:

		export VISP_INPUT_IMAGE_PATH=<my directory>

- on windows platforms:

		setx VISP_INPUT_IMAGE_PATH <my directory>

Notice the the folder <my directory> should not contain the parent directory ViSP-images. 

## Example

The following example that can be achieved on unix-like platforms allows to use the data set installed in /home/user/visp/ViSP-images:

	cd /home/user/visp
	git clone https://github.com/lagadic/ViSP-images.git
	export VISP_INPUT_IMAGE_PATH=/home/user/visp


[1]: http://visp.inria.fr "ViSP"
[2]: http://visp.inria.fr/download "ViSP download"
