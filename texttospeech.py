# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
def textToSpeech(mytext,language):
    # The text that you want to convert to audio
    mytext = mytext

    # Language in which you want to convert
    language = language

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("welcome.mp3")
    return myobj.stream()

    # Playing the converted file
    
