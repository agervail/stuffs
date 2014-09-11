# -*- coding: utf-8 -*-
#!/usr/bin/python

__author__ = 'agervail'

from datetime import datetime
from subprocess import call

d = datetime.now()
name = '/home/pi/timelapse/pictures/pic_' + d.strftime('%d-%m-%y_%H:%M:%S') + '.jpg'

print name

call(['raspistill','-vf','-hf','-w', '640', '-h', '480', '-q', '10', '-th', 'none', '-o', name])