# usage /python3 filter.py /path/to/image

import math 
import sys 

from PIL import Image, ImageFilter 

image = Image.open(sys.argv[1]).convert('RGB')

filterd = image.filter(ImageFilter.Kernel(
    size=(3,3),
    kernel=[-1,-1,-1,-1,8,-1,-1,-1,-1],
    scale=1
))

filterd.show()
