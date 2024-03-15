#-----
# Description   : Main script for performing 3D reconstruction using COLMAP
# Author        : Berkan Lafci
# E-mail        : lafciberkan@gmail.com
#-----

# import libraries
import argparse

from mvps import *

# argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--dataDir', default='data/')
parser.add_argument('--objectName', default='object')
args = parser.parse_args()

# object and image directory
databaseDir     = args.dataDir + args.objectName + '/database.db'
imageDir        = args.dataDir + args.objectName + '/images'
sparseDir       = args.dataDir + args.objectName + '/sparse'
mvsDir          = args.dataDir + args.objectName + '/mvs'
cameraMode      = 'SIMPLE_PINHOLE' # Options: PINHOLE, SIMPLE_PINHOLE, RADIAL, SIMPLE_RADIAL, OPENCV, FULL_OPENCV, SIMPLE_RADIAL_FISHEYE, RADIAL_FISHEYE, OPENCV_FISHEYE, FOV, THIN_PRISM_FISHEYE

# create colmap object
colmapObj       = ColmapManager()

# colmap feature extraction and matching
colmapObj.extractFeatures(databaseDir, imageDir, cameraMode)
colmapObj.matchFeatures(databaseDir)

# colmap sparse reconstruction
colmapObj.sparseReconstruction(databaseDir, imageDir, sparseDir)

# colmap undistort images
colmapObj.undistortImages(mvsDir, sparseDir, imageDir)

# colmap dense reconstruction (requires CUDA)
colmapObj.patchMatchStereo(mvsDir)
colmapObj.denseReconstruction(mvsDir)
colmapObj.poissonMeshing(mvsDir)
