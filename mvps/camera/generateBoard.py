#-----
# Description   : Generate checkerboard with aruco patterns
# Author        : Berkan Lafci
# E-mail        : lafciberkan@gmail.com
#-----

# import libraries
import cv2

#-------------------------------#
# user defined parameters

# name and directory for file saving
boardName       = 'checkerBoard.png' # name of the board
dataDir         = 'data/board' # data folder to save generated images

# defined dictionaries in aruco library
dictionaryName  = cv2.aruco.DICT_5X5_250 # number of small squares inside the big squares

# define board size and margins
numVertical     = 6 # number of vertical squares on board
numHorizontal   = 6 # number of horizontal squares on board

numPixels       = 1000 # number of pixels
marginPixels    = 50 # pixel numbers of side margins

sideLength      = 30 # side of the squares
gapLength       = 2 # gap between squares

#-------------------------------#
# board generation

# define board using aruco library
arucoDictionary = cv2.aruco.getPredefinedDictionary(dictionaryName) # define dictionary
checkerBoard  = cv2.aruco.GridBoard((numVertical, numHorizontal), sideLength, gapLength, arucoDictionary) # define grid board

# image generation
boardImage      = cv2.aruco.CharucoBoard.generateImage(checkerBoard, (int(numPixels*numVertical), int(numPixels*numHorizontal)), marginSize=marginPixels) # generate board image

# save checkerboard
cv2.imwrite(dataDir + '/' + boardName, boardImage) # save image
