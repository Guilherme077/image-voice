from imagevoice.tools import stringToBin

message = input("Digite uma mensagem: ")
messageBin = stringToBin(message)
print("A mensagem, em binário (8 bits) é ", messageBin)