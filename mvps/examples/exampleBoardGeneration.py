#-----
# Description   : Main script for board generation
# Author        : Berkan Lafci
# E-mail        : lafciberkan@gmail.com
#-----

# import libraries
import os
import cv2
import argparse

from mvps import *

# argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--dataDir', default='data/board')
parser.add_argument('--boardName', default='checkerboard.png')
parser.add_argument('--dictionaryName', default=cv2.aruco.DICT_5X5_250)
parser.add_argument('--numVertical', default=6)
parser.add_argument('--numHorizontal', default=2)
parser.add_argument('--numPixels', default=1000)
parser.add_argument('--marginPixels', default=50)
parser.add_argument('--sideLength', default=30)
parser.add_argument('--gapLength', default=5)
args = parser.parse_args()

# create board object
boardObject = BoardManager(dataDir=args.dataDir, boardName=args.boardName, dictionaryName=args.dictionaryName,
                        numVertical=args.numVertical, numHorizontal=args.numHorizontal, numPixels=args.numPixels,
                        marginPixels=args.marginPixels, sideLength=args.sideLength, gapLength=args.gapLength)

# generate checkerboard and save
boardObject.generateCheckerboard()

# print the directory of the saved checkerboard
print('Checkerboard is saved at: {}'.format(os.path.abspath(args.dataDir + '/' + args.boardName)))
