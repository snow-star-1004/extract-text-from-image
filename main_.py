from image2text import img2txt, area_screenshot
from pushy import doPush

import time
import os

temp_path = os.path.abspath("./temp")
try:
    os.makedirs(temp_path)
except FileExistsError:
    pass


##filename = area_screenshot(1415, 740, 1770, 800, temp_path)
filename = area_screenshot(1465, 850, 1859, 875, temp_path)
time.sleep(1)
text = img2txt(temp_path, filename)
print(text)
#if 'mythic' in text.lower():
#	print('true')
#else:
#	print('false')	
#doPush("title",text)
