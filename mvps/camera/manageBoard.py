#-----
# Description   : Board object properties and functions
# Author        : Berkan Lafci
# E-mail        : lafciberkan@gmail.com
#-----

# import libraries
import os
import cv2

class BoardManager():

    def __init__(self, dataDir='data/board', boardName='checkerBoard.png', dictionaryName=cv2.aruco.DICT_5X5_250, numVertical=6, numHorizontal=2, numPixels=1000, marginPixels=50, sideLength=30, gapLength=2):
        """
        Connect cameras by reading and saving information
        """
        
        # directory related parameters
        self._dataDir           = dataDir # data folder to save generated images
        os.makedirs(dataDir, exist_ok=True) # create directory to save board images
        self._boardName         = boardName # name of the board
        self.__boardDir         = self._dataDir + '/' + self._boardName + '.png' # directory to save board image

        # board related parameters
        self._dictionaryName    = dictionaryName # number of small squares inside the big squares

        self._numVertical       = numVertical # number of vertical squares on board
        self._numHorizontal     = numHorizontal # number of horizontal squares on board

        self._numPixels         = numPixels # number of pixels
        self._marginPixels      = marginPixels # pixel numbers of side margins

        self._sideLength        = sideLength # side of the squares
        self._gapLength         = gapLength # gap between squares


    #-------------------------------#
    #---------- functions ----------#
    #-------------------------------#

    #-------------------------------#
    # generate checkerboard

    def generateCheckerboard(self):

        # define board using aruco library
        arucoDictionary = cv2.aruco.getPredefinedDictionary(self._dictionaryName) # define dictionary
        checkerBoard    = cv2.aruco.GridBoard((self._numVertical, self._numHorizontal), self._sideLength, self._gapLength, arucoDictionary) # define grid board

        # image generation
        boardImage      = cv2.aruco.CharucoBoard.generateImage(checkerBoard, (int(self._numPixels*self._numVertical), int(self._numPixels*self._numHorizontal)), marginSize=self._marginPixels)

        # save checkerboard
        cv2.imwrite(self.__boardDir, boardImage)
