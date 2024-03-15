#-----
# Description   : Apply COLMAP for initial processing and baseline reconstruction
# Author        : Berkan Lafci
# E-mail        : lafciberkan@gmail.com
#-----

# import libraries
import pycolmap

class ColmapManager():

    def __init__(self):
        """
        PyCOLMAP functions
        """

        print('Starting PyCOLMAP process...')
    
    #-------------------------------#
    #---------- functions ----------#
    #-------------------------------#

    #-------------------------------#
    # extract features from 2D images

    def extractFeatures(self, databaseDir, imageDir, cameraMode):
        """
        Extract features from images
        """

        pycolmap.extract_features(databaseDir, imageDir, camera_model = cameraMode)

    #-------------------------------#
    # match features
        
    def matchFeatures(self, databaseDir):
        """
        Match detected features
        """

        pycolmap.match_exhaustive(databaseDir)
    
    #-------------------------------#
    # sparse reconstruction
        
    def sparseReconstruction(self, databaseDir, imageDir, sparseDir):
        """
        Sparse reconstruction/mapping
        """

        maps = pycolmap.incremental_mapping(databaseDir, imageDir, sparseDir)
        maps[0].write(sparseDir)

    #-------------------------------#
    # undistort images
    
    def undistortImages(self, mvsPath, sparseDir, imageDir):
        """
        Undistort images
        """

        pycolmap.undistort_images(mvsPath, sparseDir, imageDir)
    
    #-------------------------------#
    # patch match stereo
    
    def patchMatchStereo(self, mvsPath):
        """
        Patch match stereo
        """

        pycolmap.patch_match_stereo(mvsPath)

    #-------------------------------#
    # dense reconstruction
        
    def denseReconstruction(self, mvsPath):
        """
        Dense reconstruction
        """

        pycolmap.stereo_fusion(mvsPath + "/dense.ply", mvsPath)

    #-------------------------------#
    # poisson meshing

    def poissonMeshing(self, mvsPath):
        """
        Poisson meshing
        """

        pycolmap.poisson_meshing(mvsPath + "/dense.ply", mvsPath + "/poisson_mesh.ply")
