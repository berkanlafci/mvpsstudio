#-----
# Description   : Control light over SPI pin on Raspberry Pi 5
# Author        : Berkan Lafci
# E-mail        : lafciberkan@gmail.com
#-----

"""
Script to turn on and off pixels on the LED ring arrays

Loops are discarded to avoid any skipping in the triggers of the pixels. Pixel numbers are hard coded.

This script will be copied to the Raspberry Pi over ssh connection and run on Raspberry Pi to turn on and off pixels on the LED ring arrays
"""

import time
from lib import neopixel_spidev as nps

# parameters for the LED ring arrays
NUM_PIXELS  = 288 # 12 circles with 24 pixels
WAIT_TIME   = 3 # waiting time for acquisition in seconds

# turn on and off pixels on the LED ring arrays using SPI pin with NeoPixelSpiDev library
with nps.NeoPixelSpiDev(0, 0, n=NUM_PIXELS, pixel_order=nps.RGB) as pixels:

    #-------------------------------#
    #---------- 1st circle ---------#
    #-------------------------------#

    # turn on 4 pixels
    pixels[0] = 0xFFFFFF
    time.sleep(0.001)
    pixels[6] = 0xFFFFFF
    time.sleep(0.001)
    pixels[12] = 0xFFFFFF
    time.sleep(0.001)
    pixels[18] = 0xFFFFFF

    # wait for acquisition
    time.sleep(WAIT_TIME)

    # turn off all pixels
    pixels[0] = 0x000000
    pixels[6] = 0x000000
    pixels[12] = 0x000000
    pixels[18] = 0x000000

    #-------------------------------#
    #---------- 2nd circle ---------#
    #-------------------------------#

    # turn on 4 pixels
    pixels[24] = 0xFFFFFF
    time.sleep(0.001)
    pixels[30] = 0xFFFFFF
    time.sleep(0.001)
    pixels[36] = 0xFFFFFF
    time.sleep(0.001)
    pixels[42] = 0xFFFFFF

    # wait for acquisition
    time.sleep(WAIT_TIME)

    # turn off all pixels
    pixels[24] = 0x000000
    pixels[30] = 0x000000
    pixels[36] = 0x000000
    pixels[42] = 0x000000
    
    #-------------------------------#
    #---------- 3rd circle ---------#
    #-------------------------------#

    # turn on 4 pixels
    pixels[48] = 0xFFFFFF
    time.sleep(0.001)
    pixels[54] = 0xFFFFFF
    time.sleep(0.001)
    pixels[60] = 0xFFFFFF
    time.sleep(0.001)
    pixels[66] = 0xFFFFFF

    # wait for acquisition
    time.sleep(WAIT_TIME)

    # turn off all pixels
    pixels[48] = 0x000000
    pixels[54] = 0x000000
    pixels[60] = 0x000000
    pixels[66] = 0x000000

    #-------------------------------#
    #---------- 4th circle ---------#
    #-------------------------------#

    # turn on 4 pixels
    pixels[72] = 0xFFFFFF
    time.sleep(0.001)
    pixels[78] = 0xFFFFFF
    time.sleep(0.001)
    pixels[84] = 0xFFFFFF
    time.sleep(0.001)
    pixels[90] = 0xFFFFFF

    # wait for acquisition
    time.sleep(WAIT_TIME)

    # turn off all pixels
    pixels[72] = 0x000000
    pixels[78] = 0x000000
    pixels[84] = 0x000000
    pixels[90] = 0x000000

    #-------------------------------#
    #---------- 5th circle ---------#
    #-------------------------------#

    # turn on 4 pixels
    pixels[96] = 0xFFFFFF
    time.sleep(0.001)
    pixels[102] = 0xFFFFFF
    time.sleep(0.001)
    pixels[108] = 0xFFFFFF
    time.sleep(0.001)
    pixels[114] = 0xFFFFFF

    # wait for acquisition
    time.sleep(WAIT_TIME)

    # turn off all pixels
    pixels[96] = 0x000000
    pixels[102] = 0x000000
    pixels[108] = 0x000000
    pixels[114] = 0x000000

    #-------------------------------#
    #---------- 6th circle ---------#
    #-------------------------------#

    # turn on 4 pixels
    pixels[120] = 0xFFFFFF
    time.sleep(0.001)
    pixels[126] = 0xFFFFFF
    time.sleep(0.001)
    pixels[132] = 0xFFFFFF
    time.sleep(0.001)
    pixels[138] = 0xFFFFFF

    # wait for acquisition
    time.sleep(WAIT_TIME)

    # turn off all pixels
    pixels[120] = 0x000000
    pixels[126] = 0x000000
    pixels[132] = 0x000000
    pixels[138] = 0x000000
    
    #-------------------------------#
    #---------- 7th circle ---------#
    #-------------------------------#

    # turn on 4 pixels
    pixels[144] = 0xFFFFFF
    time.sleep(0.001)
    pixels[150] = 0xFFFFFF
    time.sleep(0.001)
    pixels[156] = 0xFFFFFF
    time.sleep(0.001)
    pixels[162] = 0xFFFFFF

    # wait for acquisition
    time.sleep(WAIT_TIME)

    # turn off all pixels
    pixels[144] = 0x000000
    pixels[150] = 0x000000
    pixels[156] = 0x000000
    pixels[162] = 0x000000

    #-------------------------------#
    #---------- 8th circle ---------#
    #-------------------------------#

    # turn on 4 pixels
    pixels[168] = 0xFFFFFF
    time.sleep(0.001)
    pixels[174] = 0xFFFFFF
    time.sleep(0.001)
    pixels[180] = 0xFFFFFF
    time.sleep(0.001)
    pixels[186] = 0xFFFFFF

    # wait for acquisition
    time.sleep(WAIT_TIME)

    # turn off all pixels
    pixels[168] = 0x000000
    pixels[174] = 0x000000
    pixels[180] = 0x000000
    pixels[186] = 0x000000


    #-------------------------------#
    #---------- 9th circle ---------#
    #-------------------------------#

    # turn on 4 pixels
    pixels[192] = 0xFFFFFF
    time.sleep(0.001)
    pixels[198] = 0xFFFFFF
    time.sleep(0.001)
    pixels[204] = 0xFFFFFF
    time.sleep(0.001)
    pixels[210] = 0xFFFFFF

    # wait for acquisition
    time.sleep(WAIT_TIME)

    # turn off all pixels
    pixels[192] = 0x000000
    pixels[198] = 0x000000
    pixels[204] = 0x000000
    pixels[210] = 0x000000

    #-------------------------------#
    #--------- 10th circle ---------#
    #-------------------------------#

    # turn on 4 pixels
    pixels[216] = 0xFFFFFF
    time.sleep(0.001)
    pixels[222] = 0xFFFFFF
    time.sleep(0.001)
    pixels[228] = 0xFFFFFF
    time.sleep(0.001)
    pixels[234] = 0xFFFFFF

    # wait for acquisition
    time.sleep(WAIT_TIME)

    # turn off all pixels
    pixels[216] = 0x000000
    pixels[222] = 0x000000
    pixels[228] = 0x000000
    pixels[234] = 0x000000
    
    #-------------------------------#
    #--------- 11th circle ---------#
    #-------------------------------#

    # turn on 4 pixels
    pixels[240] = 0xFFFFFF
    time.sleep(0.001)
    pixels[246] = 0xFFFFFF
    time.sleep(0.001)
    pixels[252] = 0xFFFFFF
    time.sleep(0.001)
    pixels[258] = 0xFFFFFF

    # wait for acquisition
    time.sleep(WAIT_TIME)

    # turn off all pixels
    pixels[240] = 0x000000
    pixels[246] = 0x000000
    pixels[252] = 0x000000
    pixels[258] = 0x000000

    #-------------------------------#
    #--------- 12th circle ---------#
    #-------------------------------#

    # turn on 4 pixels
    pixels[264] = 0xFFFFFF
    time.sleep(0.001)
    pixels[270] = 0xFFFFFF
    time.sleep(0.001)
    pixels[276] = 0xFFFFFF
    time.sleep(0.001)
    pixels[282] = 0xFFFFFF

    # wait for acquisition
    time.sleep(WAIT_TIME)

    # turn off all pixels
    pixels[264] = 0x000000
    pixels[270] = 0x000000
    pixels[276] = 0x000000
    pixels[282] = 0x000000
