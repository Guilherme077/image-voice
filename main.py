from imagevoice.encode import encodeMessage
from imagevoice.decode import decodeFromImage
from imagevoice.tools import textToSpeech
import time

print("-----IMAGE VOICE-----")
print("1 - Codificar Mensagem em Imagem")
print("2 - Decodificar Imagem")
option = input("Digite o número da opção desejada: ")
print()

if option == "1":
    imageUrl = input("Digite o nome da imagem (com tipo de arquivo): ")
    message = input("Digite uma mensagem: ")
    imageOutputUrl = input("Digite o nome da imagem (com tipo de arquivo): ")
    startedAt = time.time()
    encodeMessage(message, imageUrl, imageOutputUrl)
    timeToExecute = time.time() - startedAt
    print("Essa operação levou " + str(round(timeToExecute, 3)) + " segundos para ser concluída.")
elif option == "2":
    imageUrl = input("Digite o nome da imagem (com tipo de arquivo): ")
    startedAt = time.time()
    decodedText = decodeFromImage(imageUrl)
    timeToExecute = time.time() - startedAt
    print(decodedText)
    print("Essa operação levou " + str(round(timeToExecute, 3)) + " segundos para ser concluída.")
    textToSpeech(decodedText)


else:
    print("Insira uma opção válida!")