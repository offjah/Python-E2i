import sys

######## START OF SYSTEM CHECK ########
######## REMOVE IF THERE ARE ISSUES ########

import subprocess
from typing import Counter
import pkg_resources

def checkNeeded():
    required = {'PIL'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed
    return missing

missing = checkNeeded()

if missing:
    print("Missing needed library acquiring now.\n")
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
    secondCheck = checkNeeded
    if secondCheck:
        consent = ""
        while (consent != "OK"):
        print("There was an error acquiring needed libraries.\nContact your IT personel about \"installing python libraries\"\nTo confirm you understand type \"OK\"")
        consent= input()
######## END OF CHECK ########

from PIL import Image,ImageDraw,ImageFont

#sets up count for naming images
global imgNum
imgNum = 1

def createImage(list):
    #width and height are the desired size of the image to make
    width = 720
    height = 1280
    #opens the time and proj icons to be used in making the image
    #you can set up a if statement to determine which icon to use if you choose to add more icons
    #icons should also be sqare and scaled to 45x45 pixels
    time = Image.open("time.png")
    proj = Image.open("proj.png")
    #this creates a base image in the RGB space with (width, height) for the dimensions and white background color 
    img = Image.new('RGB', (width, height), color = (255, 255, 255))
    #sets the image font to arial
    imgfont = ImageFont.truetype("arial.ttf",36)
    #this sets up draw to be shorthand for imagedraw.draw(img) for convenience
    draw = ImageDraw.Draw(img)
    #imgfont.getsize calculates the space taken up by the text and store the values in w and h
    #gets the size of the font of the first list item
    w,h = imgfont.getsize(list[0])
    #draw.text puts the text onto the image, the paramaters are starting width, starting height, text to print, the font, color of text, alignment
    draw.text(((width-w)/2,(height-(h*2))/3),list[0],font=imgfont,fill="black",align ="center")
    w,h = imgfont.getsize(list[1])
    draw.text(((width-w)/2,(height-(h*4))/2),list[1],font=imgfont,fill="black",align ="center")
    w,h = imgfont.getsize(list[2])
    draw.text(((width-w)/2,(height-(h*7))/2),list[2],font=imgfont,fill="black",align ="center")
    w,h = imgfont.getsize(list[3])
    draw.text(((width-w)/2,(height+(h*2))/2),list[3],font=imgfont,fill="black",align ="center")
    w,h = imgfont.getsize(list[4])
    draw.text(((width-w)/2,(height+(h*5))/2),list[4],font=imgfont,fill="black",align ="left")
    w,h = imgfont.getsize(list[5])
    #these variables are used to figure out where to place the icons
    wwidth =int((width)/5)
    hheight = int((height-(h*21)/2))
    #this prints the time and project text and pastes the icons on aswell
    draw.text((wwidth+(w/2),hheight),list[5],font=imgfont,fill="black",align ="left")
    img.paste(proj,(wwidth,hheight),proj)
    wwidth = int(width-(width/2)+22)
    img.paste(time,(wwidth,hheight),time)
    draw.text((wwidth+(w/2),hheight),list[6],font=imgfont,fill="black",align ="center")

    w,h = imgfont.getsize(list[7])
    draw.text(((width-w)/2,(height-(h*4))),list[7],font=imgfont,fill="black",align ="center")
    w,h = imgfont.getsize(list[8])
    draw.text(((width-w)/2,(height-(h*2))),list[8],font=imgfont,fill="black",align ="center")
    w,h = imgfont.getsize("Learn more...")
    draw.text(((width-w)/2,(height)-(h*8)),"Learn more",font=imgfont,fill="blue",align ="center")
    
    #this will save the image
    img.save(imgNum+".png")
    imgNum = imgNum+1


fileName = str(sys.argv[1])

if (fileName==""):
    fileName = input("Enter the name of the csv document. Example: \"Quarter 1\"\n")

openfile = open(fileName,'r')
contents=(openfile.read())
openfile.close()

#Go thorugh cvs and get all coloums of row and instert into list
#Call createImage with the list from above








