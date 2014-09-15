# -*- coding: utf-8 -*-
#!/usr/bin/python

__author__ = 'agervail'
import math
from datetime import datetime
from subprocess import call
from PIL import Image, ImageFont, ImageStat
import ImageDraw

def brightness( im ):
  #im = Image.open(im_file)
  stat = ImageStat.Stat(im)
  r,g,b = stat.mean
  return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))

name = '/home/pi/dev/image_process/pic_'

argus = ['raspistill','-vf','-hf','-w', '200', '-h', '200', '-q', '10', '-th', 'none', '-t', '200']

pics = []
ss_opt = [500, 1000, 1500, 2000, 2500]
iso_opt = [200, 400, 600, 800]
'''
for ss in ss_opt:
  for iso in iso_opt:
    print 'pic ' + str(ss) + '/' + str(iso)
    pics.append(name + str(ss) + '-' + str(iso) + '.jpg')
    call(argus + ['-o', pics[-1], '-ss', str(ss), '-ISO', str(iso)])
'''


im = Image.new("RGB", (1000,800), "white")
draw = ImageDraw.Draw(im)
ff = ImageFont.truetype("arial.ttf",14)
for i, ss in enumerate(ss_opt):
  for j, iso in enumerate(iso_opt):
    print name + str(ss) + '-' + str(iso) + '.jpg'
    to_p = Image.open(name + str(ss) + '-' + str(iso) + '.jpg')
    brigh = brightness(to_p)
    w,h = to_p.size
    im.paste(to_p, (i*200, j*200, i*200 + w, j*200 + h))
    draw.text( ((i)*200, (j)*200), unicode(str(ss) + '-' + str(iso),'UTF-8'), font=ff)
    draw.text( ((i)*200, (j)*200 + 30), unicode(str(brigh),'UTF-8'), font=ff)

del draw
im.save('mix.jpg', 'JPEG')
