#!/usr/bin/env python

# import sys
import os
import json
import time
from pprint import pprint

# list_of_files=(os.listdir('/home/williamrmyers/williamrmyers/pointless/gallery_images'))
			   
# print list_of_files[::-1]


path_to_gallery = "/home/williamrmyers/williamrmyers/pointless/gallery_images/"


def getfiles(dirpath):
    a = [s for s in os.listdir(dirpath)
         if os.path.isfile(os.path.join(dirpath, s))]
    a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
    return a



media_filenames = getfiles(path_to_gallery)

media_filenames.reverse()
	
	
row_json = json.dumps(media_filenames)

print "Content-type: text/html"
print ""
# print ''' 
# <html>
# </html>'''

# print [list_of_files]

print row_json




# # This is how it should be formated
# print '["tumblr_mo7se6Thru1qcb5fko1_500.gif","UyjTj4x.gif","Trey Ratcliff - China 2011 - A Great Wall at Sunset-X2.jpg","QHmEdI9.gif","PSaJyLu.gif","LhJ8LE0.gif","IYknwGT.jpg","5yIVbBy.gif","22 - Joker 1.gif","16 - Batman The Dark Knight Returns 1.gif","1431147101014.jpg","1394906502467.png","1387865643740.jpg"]'











