from imagevoice.encode import encodeMessage

message = input("Digite uma mensagem: ")
imageUrl = input("Digite o nome da imagem (com tipo de arquivo): ")

encodeMessage(message, imageUrl)