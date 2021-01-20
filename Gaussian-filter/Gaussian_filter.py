from __future__ import print_function
from scipy.ndimage import gaussian_filter
import numpy as np
from PIL import Image

img = np.asarray(Image.open('../Klimt/Klimt.ppm'))
img_gray = np.asarray(Image.open('../Klimt/Klimt.pgm'))
print('img:', img.shape)

sigmas = [0.5, 2, 5, 7]
for sigma in sigmas:
    print('sigma:', sigma)
    # # do not filter across channels
    # https://github.com/scikit-image/scikit-image/blob/fca9f16da4bd7420245d05fa82ee51bb9677b039/skimage/filters/_gaussian.py#L12-L126
    img_blur = Image.fromarray(gaussian_filter(img, sigma=(sigma, sigma, 0), mode = 'nearest'))
    img_blur.save('Klimt_RGB_Gaussian_blur_sigma={:.1f}.png'.format(sigma))

    img_blur = Image.fromarray(gaussian_filter(img_gray, sigma=sigma, mode = 'nearest'))
    img_blur.save('Klimt_gray_Gaussian_blur_sigma={:.1f}.png'.format(sigma))