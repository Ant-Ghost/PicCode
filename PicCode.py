from PIL import Image
import os, sys
sys.path.append(".")
from additions.colours import bcolors as bc
from components.encode import stegano as en
from components.decode import stegano as dec





def main():
    #INTRO PATTERN        
    a='''



**********      *************        *******************       *******************              *******             **********          *****************
************    *************       *****         *******     *****         *******         *****     ******        ****     ***        *****************
***       ***       ****           *****            ****     *****            ****        *****         ******      ****      ***       ****
***       ***       ****          *****                     *****                       *****            ******     ****       ***      ****
***      ***        ****          ****                      ****                       ******             ******    ****        ***     **********
***********         ****          ****                      ****                       ******             ******    ****        ***     **********
***                 ****          *****                     *****                       ******           ******     ****       ***      ****
***                 ****           ******           ****     ******           ****        *****        *******      ****      ***       ****
***             *************       *******        ******     *******        ******         *****     ******        ****    ***         *****************
***             *************         ******************       ******************               *******             *********           *****************
    '''

    print(bc.HEADER+a+bc.ENDC)

    info ='''
\n\n 
Welcome to PicCode!!!!
This is program that lets you hide text in a picture. It also unhides any hidden text in a picture, given the message is hidden using this program.
    '''

    print(info)

    menu='''
\n\n
Press 1, for Hiding a message.
Press 2, for Unhide a hidden message
    '''

    print(bc.OKCYAN+menu+bc.ENDC)
    valid_input=[1,2]
    inp=0
    while not inp:
        try:
            inp = int(input("Enter your choice : "))
            if not  (inp in valid_input):
                print(bc.FAIL+"Press 1 or 2"+bc.ENDC)
                inp=0
        except:
            print(bc.FAIL+"Invalid Input"+bc.ENDC)

    if inp == 1:
        en.stegano_encode()

    elif inp == 2:
        dec.stegano_decode()



if __name__ == '__main__':
    main()

print("\n\n"+bc.OKBLUE+"Follow:"+bc.ENDC,end=' ')