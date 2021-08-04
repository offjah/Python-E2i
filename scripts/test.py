from PIL import Image,ImageDraw,ImageFont
def createImage(list):
    width = 720
    height = 1280
    time = Image.open("time.png")
    proj = Image.open("proj.png")
    img = Image.new('RGB', (width, height), color = (255, 255, 255))
    imgfont = ImageFont.truetype("arial.ttf",36)
    w,h = imgfont.getsize(list[0])
    draw = ImageDraw.Draw(img)
    #draw.text((0,0),"hello",font=imgfont,fill="red",align="right")
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

    wwidth =int((width)/5)
    hheight = int((height-(h*21)/2))

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
    
    
    img.show()
    
    
list = ["Richmond","Andan-tech","New houses","additional funds","$98,245,115","Housing","august 2020","contact@email.com","804-999-9999"]

createImage(list)