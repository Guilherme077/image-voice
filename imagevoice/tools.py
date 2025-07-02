
# Transforma uma mensagem de caracteres para código binário baseado em 8-bits
def stringToBin(message):
    messageBits = ""
    for c in message:
        asciiCode = ord(c) # Transforma cada caractere em código ASCII
        binaryCode = format(asciiCode, '08b') # Transforma o código ASCII em binário de 8-bits
        messageBits += binaryCode # Junta o binário do caractere com os outros binários dos caracteres anteriores
    return messageBits

def textToSpeech(text):
    import pyttsx3

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150) 
    engine.setProperty('volume', 0.9) 

    texto = text
    engine.say(texto)
    engine.runAndWait()
