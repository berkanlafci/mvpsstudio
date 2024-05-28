#!/bin/bash

# This script is taken and modified from the following link: https://gist.github.com/MihailCosmin/affa6b1b71b43787e9228c25fe15aeba

### verify your gpu support CUDA
lspci | grep -i nvidia

### remove old nvidia drivers
sudo apt purge nvidia* -y
sudo apt remove nvidia-* -y
sudo rm /etc/apt/sources.list.d/cuda*
sudo apt autoremove -y && sudo apt autoclean -y
sudo rm -rf /usr/local/cuda*

# update and upgrade packages
sudo apt update && sudo apt upgrade -y

# install other required packages
sudo apt install git g++ freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev

# get the PPA repository driver
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
sudo apt upgrade

# find recommended driver versions
ubuntu-drivers devices

# install nvidia driver with dependencies
sudo apt install libnvidia-common-535 libnvidia-gl-535 nvidia-driver-535 -y