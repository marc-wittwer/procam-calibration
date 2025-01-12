import numpy as np
import cv2 as cv
import glob

image_path_1 = 'capture_0/graycode_42.png'
image_path_2 = 'capture_1/graycode_42.png'
image_path_3 = 'capture_2/graycode_42.png'
image_path_4 = 'capture_3/graycode_42.png'
image_path_5 = 'capture_4/graycode_42.png'

images = [image_path_1, image_path_2, image_path_3, image_path_4, image_path_5]

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
# images = glob.glob('*.jpg')
for fname in images:
    print(fname)
    img = cv.imread(fname)
    # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.imread(fname, cv.IMREAD_GRAYSCALE)

    cv.imshow('asd', gray)
    # cv.waitKey(1000)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (10,7), None)
    # If found, add object points, image points (after refining them)
    print(ret)
    if ret == True:
        print(len(objp))
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (10,7), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(500)

ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print('img_shape', gray.shape[::-1])
print('rms', ret)
print('cam_int', mtx)
print('cam_dist', dist)
print('rotation', rvecs)
print('translation', tvecs)
# cv.destroyAllWindows()