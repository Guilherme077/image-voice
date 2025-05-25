from PIL import Image
import numpy
from imagevoice.tools import stringToBin

def decodeFromImage(imageUrl):
    imageSource = Image.open(imageUrl)
    imageArrayRGB = numpy.array(imageSource)
    imagePixels = imageArrayRGB.flatten()

    decodedMessageBits = ""
    endMessageCode = stringToBin("_!IV!_")
    
    for pixel in imagePixels:
        decodedMessageBits += str(pixel & 1)  # Pega o último bit
        if(len(decodedMessageBits) > len(endMessageCode)):
            if(decodedMessageBits[-len(endMessageCode):] == endMessageCode[-len(endMessageCode):]):
                break
    
    message = ""
    for messageByte in range(0, len(decodedMessageBits) - len(endMessageCode), 8):
        byte = decodedMessageBits[messageByte:messageByte+8]
        codeASCII = int(byte, 2)
        charASCII = chr(codeASCII)
        message += charASCII
        

    return message
