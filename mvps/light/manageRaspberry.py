#-----
# Description   : Connect to raspberry pi and run light control codes
# Author        : Berkan Lafci
# E-mail        : lafciberkan@gmail.com
#-----

# import libraries
import subprocess

class RaspberryManager():

    def __init__(self):
        """
        Object to manage raspberry pi connection and light control
        """

        # raspberry pi parameters
        self.raspberryName  = 'light' # name of the raspberry pi machine
        self.userName       = 'person' # change with your username
        self.scriptName     = 'lightControl.py' # name of the light control script
    
    #-------------------------------#
    #---------- functions ----------#
    #-------------------------------#
    
    #-------------------------------#
    # copy script to raspberry pi
        
    def copyScript(self):

        # copy light pattern script to raspberry pi
        subprocess.run(['scp', 'mvps/light/'+ self.scriptName, self.userName + '@' + self.raspberryName +':~/'])

    #-------------------------------#
    # create ssh connection to raspberry pi

    def openSshConnection(self):

        # create ssh connection process
        self.sshProcess = subprocess.Popen(['ssh', '-tt', self.raspberryName], 
                                           stdin=subprocess.PIPE, stdout = subprocess.PIPE,
                                           universal_newlines=True, bufsize=0)

    #-------------------------------#
    # run light control script on raspberry pi
         
    def runScript(self):

        # run copied light script
        self.sshProcess.stdin.write('sudo /home/'+ self.userName +'/.light/bin/python3 ~/' + self.scriptName +'\n')
