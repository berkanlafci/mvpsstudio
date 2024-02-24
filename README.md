# MVPS Studio

<p align="justify"> Multiview photometric stereo (MVPS) studio hardware and software to build a small object scanner </p>

![flowers](docs/_img/flowers.png)
\* images are generated by DALL-E 3

<p align="justify"> Multiview stereo uses images taken from multiple angles to reconstruct the geometry of the scene/object. </p>

## Hardware
[![Cameras](https://img.shields.io/badge/Cameras-Link-yellow)](https://www.mouser.ch/ProductDetail/Intel/82635DSD405?qs=Znm5pLBrcAKRij2Y1eB7yg%3D%3D)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi%204B-Link-violet)](https://www.digitec.ch/de/s1/product/raspberry-pi-4-8g-model-b-entwicklungsboard-kit-13276941?utm_source=google&utm_medium=cpc&campaignid=16472930352&adgroupid=136662242280&adid=585921168913&dgCidg=EAIaIQobChMI85HThYqPgwMV6BMGAB28iw8PEAAYAiAAEgLvSPD_BwE&gad_source=1&gclsrc=ds)
[![LED](https://img.shields.io/badge/LED_Array-Link-red)](https://www.bastelgarage.ch/dfrobot-neopixel-ring-24x-ws2812-rgb-led)

### Camera

#### Intel RealSense D405  

<p align="justify"> Intel RealSense D405 is a short range camera with depth from stereo feature. Depth from stereo is information captured by the two cameras located on the same horizontal line. The cameras can reach to sub-milimiter accuracy. </p>

## Software

<p align="justify"> 1 - Install anaconda or miniconda. Then, run the following command to install required packages: </p>

```bash
conda env create -f mvps.yml
```

<p align="justify"> 2 - Install mvps studio package provided with this repository: </p>

```bash
pip install git+https://github.com/berkanlafci/mvpsstudio.git
```

<p align="justify"> PS: This repository is still under development. Majority of the codes will be released with the paper publication. </p>