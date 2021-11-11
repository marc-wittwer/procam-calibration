# coding: UTF-8

import os
import os.path
import glob
import argparse
import cv2
import numpy as np
import json


def main():

    # load image
    # detect chessboard corners


    image_path = './capture_0/graycode_43.png'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    chess_shape = (7,10)

    res, cam_corners = cv2.findChessboardCorners(image, chess_shape)

    print('res',res)
    print('corners', cam_corners)
    if not res:
        print('Error : chessboard was not found')



if __name__ == '__main__':
    main()
