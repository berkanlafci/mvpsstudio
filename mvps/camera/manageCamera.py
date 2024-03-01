#-----
# Description   : Camera object properties and functions
# Author        : Berkan Lafci
# E-mail        : lafciberkan@gmail.com
#-----

# import libraries
import os
import sys
import numpy as np
import pyrealsense2 as rs
import matplotlib.pyplot as plt

class CameraManager():

    def __init__(self, recordRGB=True, recordDepth=False):
        """
        Camera environment initialization
        """
        
        self.cameraConfig       = rs.config()
        self.cameraContext      = rs.context()

        self.connectedDevices   = {} # store device info
        self.enabledDevices     = {} # store enabled devices

        if recordRGB:
            self.cameraConfig.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 5) # enable stream of RGB

    #-------------------------------#
    #---------- functions ----------#
    #-------------------------------#

    #-------------------------------#
    # connect cameras
        
    def connectCamera(self, verbose=False):
        """
        Connect cameras by reading and saving information
        """
        
        if verbose:
            print('-------------------------------------------')
            print('Connecting cameras and parsing information!')
            print('-------------------------------------------')

        for device in self.cameraContext.devices:
            # get info of connected devices and save them
            productLine     = device.get_info(rs.camera_info.product_line)
            serialNumber    = device.get_info(rs.camera_info.serial_number)
            self.connectedDevices[serialNumber] = productLine

            if verbose:
                print('Connected Device Product Line: {}, Connected Device Serial Number: {}'.format(productLine, serialNumber))

    #-------------------------------#
    # enable cameras

    def enableCamera(self, verbose=True):
        """
        Enable connected cameras sequentially by serial number
        """

        if verbose:
            print('---------------------------------')
            print('Enabling cameras for acquisition!')
            print('---------------------------------')

        for serialNumber in self.connectedDevices:
            # enable connected devices
            pipeline                            = rs.pipeline()
            self.cameraConfig.enable_device(serialNumber)
            pipelineProfile                     = pipeline.start(self.cameraConfig)
            self.enabledDevices[serialNumber]   = (pipeline, pipelineProfile, self.connectedDevices[serialNumber])

            if verbose:
                print('Enabled Device Product Line: {}, Enabled Device Serial Number: {}'.format(self.connectedDevices[serialNumber], serialNumber))

    #-------------------------------#
    # acquire stream of images

    def acquireStream(self, acquisitionDir):
        """
        Acquire stream from connected cameras

        :param acquisitionDir:      Directory to save recorded images
        """

        imageCounter = 1

        # create directory to save images (if directory exists, it will give error and exit)
        try:
            os.makedirs(acquisitionDir, exist_ok=False)
        except OSError:
            sys.exit('Directory already exist! Please choose a different object name. Acquisition stopped!')

        # acquire until stopped with keyboard interrupt
        while True:
            for serialNumber in self.enabledDevices:
                pipeline    = self.enabledDevices[serialNumber][0]
                frameSet    = pipeline.poll_for_frames()
                rgbImage    = frameSet.get_color_frame()

                if not rgbImage:
                    continue

                numpyImage = np.asanyarray(rgbImage.get_data())

                self.saveImage(numpyImage, acquisitionDir, imageCounter)
                
                imageCounter += 1
    #-------------------------------#
    # save images
    
    def saveImage(self, numpyImage, acquisitionDir, imageCounter):
        """
        Acquire stream from connected cameras

        :param numpyImage:          Image in numpy array format
        :param acquisitionDir:      Directory to save recorded images
        :param imageCounter:        Counter for image number
        """

        # plot and save image
        plt.figure(frameon=False) # create figure
        plt.imshow(numpyImage) # plot image
        plt.axis('off') # turn off axis
        plt.savefig(acquisitionDir +'/image'+str(imageCounter)+'.png', dpi=150, bbox_inches='tight', pad_inches=0) # save image
        plt.close() # close figure