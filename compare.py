from PIL import Image
from pytesseract import pytesseract

def compare_traits(img):
    #Define path to tessaract.exe
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    #Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract

    width, height = img.size

    left = 0.695 * width
    top = 0.574 * height
    right = 0.833 * width
    bottom = 0.752 * height


    im1 = img.crop((left, top, right, bottom))

    # im1.show()
    #Extract text from image
    text = pytesseract.image_to_string(im1)
    x = text.rsplit("\n")
    txt = []
    for a in x:
        if not a == '':
            txt.append(a)
    txt.remove('SWAP WEAPON')
    traits =  txt

    config_list = []
    #for example:
    config_list.append('LEECH ROUNDS')
    # print('traits: ', traits)
    # print('config_list: ', config_list)
    flag = False
    for trait in traits:
        for value in config_list:
            if trait == value:                
                flag = True
    return flag
    
 


#Define path to image
#Open image with PIL
path_to_image = 'image.png'
imag = Image.open(path_to_image)
print(compare_traits(imag))








