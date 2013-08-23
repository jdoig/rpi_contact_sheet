===========================================
Raspberry Pi Camera Contact Sheet Generator
===========================================

This Python script for use with the Raspberry Pi was inspired by raspberrypi-spy_. 

.. _raspberrypi-spy: http://www.raspberrypi-spy.co.uk/2013/06/testing-multiple-pi-camera-options-with-python/

It takes a range of Raspberry_Pi camera settings, generates a list of all
possible combinations then takes a sample shot with each one. It then builds a
contact sheet of all the images, labeled with the settings used and copies the
sheet to a location that can be hosted by my Raspberry Pi web server
(/var/www in my case)

You may want to tweak this script by:

- Adding more combinations of settings (like raspberrypi-spi's original the
  code contains various commented out variations on the defaults)

- Adding argparse arguments to change settings, etc

- Making the subprocess calls safer by refactoring out the dependency
  on 'shell=True'

- Using larger sample images


Requires
--------

- Image Magick::

    sudo apt-get install imagemagick


Workflow
--------
You don't need to do this bit but I found it made my life a lot easier...


1. set up ssh: http://learn.adafruit.com/adafruits-raspberry-pi-lesson-6-using-ssh/enabling-ssh

2. set up a static ip address for your pi:
   https://www.modmypi.com/blog/tutorial-how-to-give-your-raspberry-pi-a-static-ip-addres

3. edit hosts on your desktop/laptop to add the ip address you assigned to your
   pi and name you want to use for your pi e.g::

    192.168.0.140   rpi

4. Install a lightweight web server on your pi::

    sudo apt-get -y install lighttpd
    sudo chown www-data:www-data /var/www
    sudo chmod 775 /var/www
    sudo usermod -a -G www-data pi
    sudo reboot

5. (assuming you called your pi: rpi in the hosts file) ::

    ssh pi@rpi 
    sudo python cs.py

...wait...

On your machine: point your web browser at rpi/contact_sheet.jpg, view the
samples, make note of the settings from the sample labels, configure your
camera and carry on shooting.


Usage
-----
::

    sudo python cs.py
