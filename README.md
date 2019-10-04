# Raspberry Pi Backup Camera
Raspberry Pi based car backup camera, streaming live video to your smart phone.

# Parts:
## Computer Requirements
1. Raspberry Pi 3 or Zero W (add link)
2. Rasperry Pi compatible camera. Wide angle lens recommended (add link)

## Optional Parts for Car Mounting
1. 12V - 5V LDO (add link)
2. Various jumper wires/splicers 
3. 3D printed camera mount (add link)
4. 3D printed casing (add link)

# RPi Setup
1. Install NOOBs image on SD card and follow directions for setup [here](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/3)
    * Raspian Full Image
2. Update Raspian, ensure ssh is enabled
3. Configure WiFi to run in Access Point mode to create a local wifi network: [here](https://thepi.io/how-to-use-your-raspberry-pi-as-a-wireless-access-point/) - Note: can skip step 8
4. Now, when booting the Pi, it should create the wifi network and you should be able to join with your phone/computer
5. [Command to generate H.264 raw video stream and place in init files]

# Mobile App Setup
1. Download Android App: https://play.google.com/store/apps/details?id=ca.frozen.rpicameraviewer&hl=en_US
1b. For iOS, try: https://apps.apple.com/us/app/rpi-camera-viewer/id1312142156 (untested)
2. Source code for mobile apps: https://github.com/ShawnBaker/RPiCameraViewer and https://github.com/ShawnBaker/iOS_RPiCameraViewer
