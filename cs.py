#!/usr/bin python
import os, sys, shutil
from glob import glob
from subprocess import call
# Full list of Exposure and White Balance options
#exs = ['off','auto','night','nightpreview','backlight',
#            'spotlight','sports','snow','beach','verylong',
#            'fixedfps','antishake','fireworks']
#awbs = ['off','auto','sun','cloud','shade','tungsten',
#            'fluorescent','incandescent','flash','horizon']
 
# Refined list of Exposure and White Balance options. 50 photos.
exs = ['off','auto','night','backlight','fireworks']
awbs = ['off','auto','sun','cloud','shade','tungsten',
            'fluorescent','incandescent','flash','horizon']
 
# Test list of Exposure and White Balance options. 6 photos.
#exs = ['off','auto']
#awbs = ['off','auto','sun']

# templates for image capture & contact sheet commands
img_cmd = 'raspistill -o /tmp/{file} -t {delay} -w {width} -h {height} -ev {ev} -ex {ex} -awb {awb}'
cs_cmd = 'montage -label "%t" "{}" -geometry +2+2 contact_sheet.jpg'
output_dir =  sys.argv[1] if len(sys.argv) > 1 else '/var/www'

#temp location of images
img_dump = '/tmp/ex_*_awb_*.jpg'

args = {
    'delay'  : 1,   
    'width'  : 320,
    'height' : 240,
    'ev'     : 0
}       

#build a list of all combinations of our options
dynamic_args = [{
        'ex' : ex, 
        'awb' : awb, 
        'file':'ex_{}_awb_{}.jpg'.format(ex,awb) 
        } for ex in exs for awb in awbs ]

def take_photos():
    for i, darg in enumerate(dynamic_args):
        print "[photo {} of {}]".format(i+1, len(dynamic_args))
        args_cat = args.copy() # make local copy of args
        args_cat.update(darg)  # merge args and dynamic args
        command = img_cmd.format(**args_cat) # format cmd string with arg dictionary
        call(command, shell=True)
try:
    
    print "Starting photo sequence"
    take_photos()
    
    print "Building contact sheet"
    call(cs_cmd.format(img_dump), shell=True)

    if output_dir:
        shutil.copy('contact_sheet.jpg', output_dir)

except KeyboardInterrupt:
        print "\nGoodbye"

finally :
    for f in glob(img_dump) :
        os.remove(f)
