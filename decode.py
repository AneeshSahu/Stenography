from PIL import Image 
import os.path,sys


def unBitAt(bits):
    num=0
    for i in range(0,len(bits)):
        num = num + bits[i]*(2**(7-i))
    return chr(num)


def add(color,bits):
    bit = color%2
    bits.append(bit)
    if len(bits)==8:
        num = unBitAt(bits)
        bits.clear()
        if ord(num)!=0:
            return num
    return ""

def decode(imgFile):
    print("Decoding {:s}".format(imgFile))
    try:
        im = Image.open(imgFile)
        pix = im.load()
    except Exception as e:
        print("Could not open image.")
        print(e)
        return
    fileParts = os.path.splitext(imgFile)
    newFile = fileParts[0]+"_decoded.txt"
    try:
        output=open(newFile,"w")
    except Exception as e:
        print("Cannot open file to write.")
        print(e)
        return
    xMax = im.size[0]
    yMax = im.size[1]
    bits=[]
    for y in range(0,yMax):
        for x in range(0,xMax):
            r = pix[x,y][0]
            output.write(add(r,bits))
            g = pix[x,y][1]
            output.write(add(g,bits))
            b = pix[x,y][2]
            output.write(add(b,bits))
    output.close()
    print("Output Written to {:s}".format(newFile))
if __name__ =="__main__":
    if len(sys.argv)!=2:
        print("Usage: python3 decode.py [image.bmp]")
        sys.exit(0)
    img = sys.argv[1]
    decode(img)