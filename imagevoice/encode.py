from PIL import Image
import numpy
from imagevoice.tools import stringToBin

# Insere uma mensagem em uma imagem
def encodeMessage(message, imageUrl):

    # Processamento da mensagem
    message += "_!IV!_" # Adiciona o código que identifica o fim da mensagem
    messageBinary = stringToBin(message) # Transforma a mensagem em código binário

    # Processamento da imagem
    inputImage = Image.open(imageUrl) # Abre a imagem a partir do nome
    imageArrayRGB = numpy.array(inputImage) # Obtém uma matriz tridimensional dos valores RGB da imagem (linhas, colunas, RGB)
    imagePixels = imageArrayRGB.flatten() # Tranforma a matriz tridimensional em uma lista única de valores RGB

    print("A imagem possui capacidade de ", len(imagePixels), " bits de mensagem")
    print("A mensagem possui tamanho de ", len(messageBinary), " bits")

    # Inserir bits da mensagem na imagem
    for bitIndex in len(messageBinary):
        originalPixelImage = imagePixels[bitIndex] # Valor original do canal de cor do pixel (RGB)
        bitMessage = messageBinary[bitIndex] # Bit que será registrado na imagem
        
        # Se o bit que será registrado é 0 e o valor do canal de cor da imagem é ímpar...
        if(bitMessage == 0 and originalPixelImage % 2 != 0):
            originalPixelImage += 1 # O valor do canal de cor deve ser par

        # Se o bit que será registrado é 1 e o valor do canal de cor da imagem é par...
        if(bitMessage == 1 and originalPixelImage % 2 == 0):
            originalPixelImage += 1 # O valor do canal de cor deve ser ímpar

    # Converter os valores para arquivo de imagem e salvar
    imageEncoded = imagePixels.reshape(imageArrayRGB.shape)
    imageWithMessage = Image.fromarray(imageEncoded.astype('uint8'))
    imageWithMessage.save("encoded_img.png")