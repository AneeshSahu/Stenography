from PIL import Image

import os.path,sys,rsa

def createDigest(textfile):
    (public, private) = rsa.newkeys(1024)
    #digest = str(private)
    digest = str()
    #key = open("private_key","w")
    #key.write(str(private))
    #key.close()
    with open(textfile,'r') as txt :
        for chunk in txt:
            digest += str(rsa.encrypt(chunk.encode('utf8'),public))
    return digest
    #return open(textfile).read()

def bitAt(pos,text):
    if pos > len(text):
        return 0
    target = pos//8
    bit = pos%8
    letter = ord(text[target])
    targetBit = int(2**(7-bit))
    if(targetBit & letter) == targetBit :
        return 1
    return 0

def scrambleBit(colour,bit):
    if colour%2 == bit%2:
        return colour
    elif colour == 0:
        colour+=1
    else :
        colour -=1
    return colour

    
def sten(image,text):
    im = Image.open(image)
    pix = im.load()
    xMax = im.size[0]
    yMax = im.size[1]
    current =0

    for y in range(0,yMax):
        for x in range(0,xMax):
            r = pix[x,y][0]
            nextBit = bitAt(current,text)
            r = scrambleBit(r,nextBit)
            current += 1
            g = pix[x,y][1]
            nextBit = bitAt(current,text)
            g = scrambleBit(g,nextBit)
            current += 1
            b = pix[x,y][2]
            nextBit = bitAt(current,text)
            b = scrambleBit(b,nextBit)
            current += 1
            pix[x,y]= (r,g,b)
    im.save("dal_makhani.bmp")

if __name__ =="__main__":
    imageOrigin = sys.argv[1]
    text= sys.argv[2]
    digest = createDigest(text)
    sten(imageOrigin,digest)
