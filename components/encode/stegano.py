from PIL import Image
import os, sys
sys.path.append("../../")
from additions.colours import bcolors as bc

def msg_to_bytes(msg):

    if type(msg)==str:
        return ''.join([format(ord(i),"08b") for i in msg])

    if type(msg)==tuple:
        return [format(i,'08b') for i in msg]
    
    if type(msg)==int:
        return format(msg,'08b')




def encode(im, msg):
    pixels=im.load()
    pixels_list=list(im.getdata())
    index_p=0
    index_msg=0

    bytes_msg=msg_to_bytes(msg)
    #print(bytes_msg)


    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if (index_msg==len(bytes_msg)):
                return

            
            pixel_arr=msg_to_bytes(pixels_list[index_p])
            #r,g,b,a =msg_to_bytes(pixels_list[index_p])
            index_p+=1
            
            
            
            for x in range(0,len(pixel_arr)):
                
                if index_msg<len(bytes_msg):
                    pixel_arr[x]=pixel_arr[x][:-1]+bytes_msg[index_msg]
                    index_msg+=1
                pixel_arr[x]=int(pixel_arr[x],2)
            pixels[j,i]=tuple(pixel_arr)
            '''
            
            if index_msg<len(bytes_msg):
                r = int(r[:-1]+bytes_msg[index_msg],2)
                index_msg+=1

            if index_msg<len(bytes_msg):
                g= int(g[:-1]+bytes_msg[index_msg],2)
                index_msg+=1

            if index_msg<len(bytes_msg):
                b = int(b[:-1]+bytes_msg[index_msg],2)
                index_msg+=1

            if index_msg<len(bytes_msg):
                a = int(a[:-1]+bytes_msg[index_msg],2)
                index_msg+=1
            
            pixels[j,i] = (r,g,b,a)
            '''
            #input()


def stegano_encode():
    
    secret_message=''
    
    #Input Message and its Checking
    while True:
        print(bc.WARNING+"Your message must not contain hash(#)"+bc.ENDC+bc.ENDC)
        print(bc.WARNING+"8 character will be padded to the given message"+bc.ENDC+bc.ENDC)
        secret_message=input("Enter your message: ")

        print("Checking validity of your messsage....", end='')
        if '#' in secret_message:
            print(bc.FAIL+"Invalid"+bc.ENDC)
        else:
            print(bc.OKGREEN+"OK"+bc.ENDC)
            break
    secret_message="####"+secret_message+"####"
    
   #Input Image path and its Checking
    while True:
        im_path=input("Enter path of image: ")
        print("Checking path....", end='')
        if os.path.exists(im_path):
            print(bc.OKGREEN+"Exist"+bc.ENDC)
            break
        else:
            print(bc.FAIL+"Invalid"+bc.ENDC)
    
    #Opening Image
    im = Image.open(im_path)

    f= im.format
    if f=='JPEG':
        print(bc.FAIL+"JPEG not allowed .... Exiting"+bc.ENDC)
        return

    if not (im.mode=='RGB' or im.mode=='RGBA'):
        print(bc.FAIL+"Only RGB or RGBA modes supported..... Exiting"+bc.ENDC)
        return

    fn, fext= os.path.splitext(im_path)
    
    #Comparing image size(pixels) and message length(characters) [no. of pixels >= no. of characters]
    print("Comparing Image size and Message Length...",end='')
    w, h= im.size
    size=w*h
    if size < len(secret_message):
        print(bc.FAIL+"Image too small to encrypt - change message size or file size\nExiting...."+bc.ENDC)
        return
    print(bc.OKGREEN+"Image size is good"+bc.ENDC)

    encode(im, secret_message)
    
    new_save= fn+"_encode"+fext

    #print(list(im.getdata())[:10])

    im.save(new_save,f)

    print(bc.OKGREEN+"Encoding done"+bc.ENDC+"...Image saved at "+new_save)
    im.close()

    return


