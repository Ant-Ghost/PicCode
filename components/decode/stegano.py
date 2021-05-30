from PIL import Image
import os, sys
sys.path.append("../../")
from additions.colours import bcolors as bc


def decideAndShow(bytes_decode):



    if len(bytes_decode)==8*4:
        four_char=''
        four_char_decode=[bytes_decode[i:i+8] for i in range(0, len(bytes_decode), 8)]
        for i in four_char_decode:
            four_char+=chr(int(i,2))
            if not ('#' in four_char):
                print("Image has no hidden text")
                return True
                
    text_decode=[bytes_decode[i:i+8] for i in range(0, len(bytes_decode), 8)]
    
    text = ''
    for i in text_decode:
        text+=chr(int(i,2))
        if len(text) > 4:
    	    if text[-4:]=='####':
		        print("\n\nText decode: " + text[4:-4])
		        return True

    return False


def decode(im):
    pixels_list=list(im.getdata())
    index=0
    bytes_decode=''
    while True:
        pixel_tuple= pixels_list[index]
                
        for i in range(0,len(pixel_tuple)):
            bytes_decode+= str(pixel_tuple[i]&1)
            if len(bytes_decode)>=8*4 and len(bytes_decode)%8==0 and decideAndShow(bytes_decode):
                return
        
        '''
        bytes_decode+= str(r&1)
        bytes_decode+= str(g&1)
        bytes_decode+= str(b&1)
        bytes_decode+= str(a&1)
        
        print(bytes_decode)


        if len(bytes_decode)>=8*4 and len(bytes_decode)%8==0 and decideAndShow(bytes_decode):
                return
        '''
        index+=1




def stegano_decode():
    
    #Input Image path and its Checking
    while True:
        im_path=input("Enter path of image: ")
        print("Checking path....", end='')
        if os.path.exists(im_path):
            print(bc.OKGREEN+"Exist"+bc.ENDC)
            break
        else:
            print(bc.FAIL+"Invalid"+bc.ENDC)

    im = Image.open(im_path)
    decode(im)
    im = im.close()


