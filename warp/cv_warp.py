from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np

def affine(img, M, filename, shape=None):
    if len(np.array(img).shape) == 2:
        color = False
    else:
        color = True
    if shape is None:
        shape = (img.shape[1], img.shape[0])

    img_warp = cv.warpAffine(img, M, shape, flags=cv.INTER_NEAREST)
    if color:
        cv.imwrite(filename + '_color_NN.png', img_warp)
    else:
        cv.imwrite(filename + '_gray_NN.png', img_warp)

    img_warp = cv.warpAffine(img, M, shape, flags=cv.INTER_LINEAR)
    if color:
        cv.imwrite(filename + '_color_bilinear.png', img_warp)
    else:
        cv.imwrite(filename + '_gray_bilinear.png', img_warp)

def perspective(img, M, filename, shape=None):
    if len(np.array(img).shape) == 2:
        color = False
    else:
        color = True
    if shape is None:
        shape = (img.shape[1], img.shape[0])

    img_warp = cv.warpPerspective(img, M, shape, flags=cv.INTER_NEAREST)
    if color:
        cv.imwrite(filename + '_color_NN.png', img_warp)
    else:
        cv.imwrite(filename + '_gray_NN.png', img_warp)

    img_warp = cv.warpPerspective(img, M, shape, flags=cv.INTER_LINEAR)
    if color:
        cv.imwrite(filename + '_color_bilinear.png', img_warp)
    else:
        cv.imwrite(filename + '_gray_bilinear.png', img_warp)

def main():
    print('cv.__version__', cv.__version__)

    img_color = cv.imread('../Klimt/Klimt.ppm')
    print('img_color:', img_color.shape)

    img_gray = cv.imread('../Klimt/Klimt.pgm', cv.IMREAD_GRAYSCALE)
    print('img_gray:', img_gray.shape)

    # Rotation of 45°
    angle = np.radians(45)
    M_rot_45 = np.array([[np.cos(angle), -np.sin(angle), img_color.shape[1] / 2],
                         [np.sin(angle),  np.cos(angle), img_color.shape[0] / 2]])
    print('M_rot_45:\n', M_rot_45)

    affine(img_color, M_rot_45, 'cv_warp_affine_rot_45')
    affine(img_gray, M_rot_45, 'cv_warp_affine_rot_45')

    # SRT
    s = 0.83
    angle = np.radians(-67)
    tx = img_color.shape[1] / 2 + 17
    ty = img_color.shape[0] / 2 - 23
    M_SRT = np.array([[s*np.cos(angle), -s*np.sin(angle), tx],
                      [s*np.sin(angle),  s*np.cos(angle), ty]])
    print('M_SRT:\n', M_SRT)

    affine(img_color, M_SRT, 'cv_warp_affine_SRT')
    affine(img_gray, M_SRT, 'cv_warp_affine_SRT')

    # Homography
    H = np.array([[1.8548, -0.0402, 114.9],
                  [1.1209, 4.0106, 111],
                  [0.0022, 0.0064, 1]])
    print('H:\n', H)

    perspective(img_color, H, 'cv_warp_perspective')
    perspective(img_gray, H, 'cv_warp_perspective')

    ## Rotation of -90°
    ## Crop image
    #img_color = img_color[0:img_color.shape[0]//2,:]
    #s = 1
    #angle = np.radians(-90)
    #alpha = s * np.cos(angle)
    #beta = s * np.sin(angle)
    #center_x = img_color.shape[1] / 2
    #center_y = img_color.shape[0] / 2
    #M_rot_90 = np.array([[alpha, beta, 0],
                         #[-beta, alpha, 0]])
    #M_rot_90[0,2] = (1 - M_rot_90[0,0] - M_rot_90[0,1]) * center_x
    #M_rot_90[1,2] = (1 - M_rot_90[1,0] - M_rot_90[1,1]) * center_y
    #print('M_rot_90:\n', M_rot_90)

    #affine(img_color, M_rot_90, 'cv_warp_affine_rot_90', (img_color.shape[1], img_color.shape[1]))

if __name__ == "__main__":
    main()
