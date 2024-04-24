#-----
# Description   : Main script for acquisition
# Author        : Berkan Lafci
# E-mail        : lafciberkan@gmail.com
#-----

# import libraries
import os
import time
import argparse

from mvps import *

# argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--dataDir', default='data/')
parser.add_argument('--objectName', default='object')
args = parser.parse_args()

# image acquisition directory
acquisitionDir  = args.dataDir + args.objectName + '/images'

# create a camera object
cameraObj = CameraManager()
cameraObj.connectCamera(verbose=False)
cameraObj.enableCamera(verbose=True)

# create light object
lightObj = RaspberryManager()
lightObj.copyScript()
lightObj.openSshConnection()
lightObj.runScript()

# wait for a while until the lights are on
time.sleep(2)

# start scanning
try:
    # acquire images until stopped
    print('----------------')
    print('Start acquiring!')
    print('----------------')

    # acquire images until stopped
    cameraObj.acquireStream(acquisitionDir)

# stop image acquistion and disable cameras     
except KeyboardInterrupt:
    print('\n--------------------')
    print('Acquisition stopped!')
    print('--------------------')
    cameraObj.cameraConfig.disable_all_streams()

    print('Images are saved at: {}'.format(os.path.abspath(acquisitionDir)))
