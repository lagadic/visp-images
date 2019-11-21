from __future__ import print_function
from __future__ import division
import PIL as PIL
from PIL import Image
import numpy as np

def affine(img, M, filename, shape=None):
    if len(np.array(img).shape) == 2:
        color = False
    else:
        color = True
    if shape is None:
        shape = img.size

    pil_aff_params = list(np.linalg.inv(M).ravel()[0:6])

    img_warp = img.transform(shape, Image.AFFINE, pil_aff_params, Image.NEAREST)
    if color:
        img_warp.save(filename + '_color_NN.png')
    else:
        img_warp.save(filename + '_gray_NN.png')

    img_warp = img.transform(shape, Image.AFFINE, pil_aff_params, Image.BILINEAR)
    if color:
        img_warp.save(filename + '_color_bilinear.png')
    else:
        img_warp.save(filename + '_gray_bilinear.png')

def perspective(img, M, filename, shape=None):
    if len(np.array(img).shape) == 2:
        color = False
    else:
        color = True
    if shape is None:
        shape = img.size

    M_inv = np.linalg.inv(M)
    M_inv = M_inv / M_inv[2,2]
    pil_pers_params = list(M_inv.ravel()[0:8])

    img_warp = img.transform(shape, Image.PERSPECTIVE, pil_pers_params, Image.NEAREST)
    if color:
        img_warp.save(filename + '_color_NN.png')
    else:
        img_warp.save(filename + '_gray_NN.png')

    img_warp = img.transform(shape, Image.PERSPECTIVE, pil_pers_params, Image.BILINEAR)
    if color:
        img_warp.save(filename + '_color_bilinear.png')
    else:
        img_warp.save(filename + '_gray_bilinear.png')

def main():
    print('PIL.__version__', PIL.__version__)

    img_color = Image.open('../Klimt/Klimt.ppm')
    print('img_color:', np.array(img_color).shape)

    img_gray = Image.open('../Klimt/Klimt.pgm')
    print('img_gray:', np.array(img_gray).shape)

    # Rotation of 45°
    angle = np.radians(45)
    M_rot_45 = np.array([[np.cos(angle), -np.sin(angle), img_color.width / 2],
                         [np.sin(angle),  np.cos(angle), img_color.height / 2],
                         [0,0,1]])
    print('M_rot_45:\n', M_rot_45)

    affine(img_color, M_rot_45, 'pil_warp_affine_rot_45')
    affine(img_gray, M_rot_45, 'pil_warp_affine_rot_45')

    # SRT
    s = 0.83
    angle = np.radians(-67)
    tx = img_color.width / 2 + 17
    ty = img_color.height / 2 - 23
    M_SRT = np.array([[s*np.cos(angle), -s*np.sin(angle), tx],
                      [s*np.sin(angle),  s*np.cos(angle), ty],
                      [0,0,1]])
    print('M_SRT:\n', M_SRT)

    affine(img_color, M_SRT, 'pil_warp_affine_SRT')
    affine(img_gray, M_SRT, 'pil_warp_affine_SRT')

    # Homography
    H = np.array([[1.8548, -0.0402, 114.9],
                  [1.1209, 4.0106, 111],
                  [0.0022, 0.0064, 1]])
    print('H:\n', H)

    perspective(img_color, H, 'pil_warp_perspective')
    perspective(img_gray, H, 'pil_warp_perspective')

    ## Rotation of -90°
    ## Crop image
    #np_img = np.asarray(img_color)
    #np_img = np_img[0:np_img.shape[0]//2,:]
    #img_color = Image.fromarray(np_img)
    #s = 1
    #angle = np.radians(-90)
    #alpha = s * np.cos(angle)
    #beta = s * np.sin(angle)
    #center_x = img_color.width / 2
    #center_y = img_color.height / 2
    #M_rot_90 = np.array([[alpha, beta, 0],
                         #[-beta, alpha, 0],
                         #[0,0,1]])
    #M_rot_90[0,2] = (1 - M_rot_90[0,0] - M_rot_90[0,1]) * center_x
    #M_rot_90[1,2] = (1 - M_rot_90[1,0] - M_rot_90[1,1]) * center_y
    #print('M_rot_90:\n', M_rot_90)

    #affine(img_color, M_rot_90, 'pil_warp_affine_rot_90', (img_color.width, img_color.width))

if __name__ == "__main__":
    main()
