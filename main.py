from imagevoice.encode import encodeMessage
from imagevoice.decode import decodeFromImage

message = input("Digite uma mensagem: ")
imageUrl = input("Digite o nome da imagem (com tipo de arquivo): ")

encodeMessage(message, imageUrl)
print(decodeFromImage("encoded_img.png"))