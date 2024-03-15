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
    
    def undistortImages(self, mvpsPath, sparseDir, imageDir):
        """
        Undistort images
        """

        pycolmap.undistort_images(mvpsPath, sparseDir, imageDir)
    
    #-------------------------------#
    # patch match stereo
    
    def patchMatchStereo(self, mvpsPath):
        """
        Patch match stereo
        """

        pycolmap.patch_match_stereo(mvpsPath)

    #-------------------------------#
    # dense reconstruction
        
    def denseReconstruction(self, mvpsPath):
        """
        Dense reconstruction
        """

        pycolmap.stereo_fusion(mvpsPath + "/dense.ply", mvpsPath)

    #-------------------------------#
    # poisson meshing

    def poissonMeshing(self, mvpsPath):
        """
        Poisson meshing
        """

        pycolmap.poisson_meshing(mvpsPath + "/dense.ply", mvpsPath + "/poisson_mesh.ply")
