from imagevoice.encode import encodeMessage
from imagevoice.decode import decodeFromImage
from imagevoice.tools import textToSpeech

print("-----IMAGE VOICE-----")
print("1 - Codificar Mensagem em Imagem")
print("2 - Decodificar Imagem")
option = input("Digite o número da opção desejada: ")
print()

if option == "1":
    imageUrl = input("Digite o nome da imagem (com tipo de arquivo): ")
    message = input("Digite uma mensagem: ")
    imageOutputUrl = input("Digite o nome da imagem (com tipo de arquivo): ")
    encodeMessage(message, imageUrl, imageOutputUrl)
elif option == "2":
    imageUrl = input("Digite o nome da imagem (com tipo de arquivo): ")
    decodedText = decodeFromImage(imageUrl)
    print(decodedText)
    textToSpeech(decodedText)


else:
    print("Insira uma opção válida!")