import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import language_tool_python  
from gtts import gTTS
from io import BytesIO
import pygame
import time 

# # Source: https://github.com/olaDEN

colT1,colT2 = st.columns([1,3])
with colT2:
    st.title("GrammarBot")


st.write("Hey there \U0001F44B \U0001F603 please click the \"Speak\" button and say something, i will check your grammar \U0001F609. ")

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
mic = sr.Microphone()
left, center, center2, right, right2 = st.columns(5)

isspeak = center2.button("Speak")

with mic as source:
    if isspeak:  
        audio = recognizer.adjust_for_ambient_noise(source, duration=0.2)
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source, timeout=3, phrase_time_limit=8)
        try:
            # take user input
            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            def speak(text, language='en'):
                mp3_fo = BytesIO()
                tts = gTTS(text, lang=language)
                tts.write_to_fp(mp3_fo)
                pygame.mixer.music.load(mp3_fo, 'mp3')
                time.sleep(0.1)
                pygame.mixer.music.play()
                # return mp3_fo
                
            # creating the tool  
            my_tool = language_tool_python.LanguageTool('en-US', config={ 'cacheSize': 1000, 'pipelineCaching': True })  
            # given text  
            my_text = my_tool.correct(text)
            # correction 
            if len(my_text)==len(text):
              st.markdown(f"## GrammarBot reply:")
              correct_text = "You said \"" + text + "\" and it is correct."
              pygame.init()
              pygame.mixer.init()
              # sound.seek(0)
              output = speak(correct_text)
              st.success(f"{correct_text}") 
            else:
              # <h1 style='text-align: center; color: red;'>GrammarBot reply:</h1>
              st.markdown("GrammarBot reply:", unsafe_allow_html=True)
              correct_text = "The correct way to say that: \"" + my_text + "\""
              pygame.init()
              pygame.mixer.init()
              # sound.seek(0)
              output = speak(correct_text)
              st.success(f"{correct_text}") 
              st.error(f"What you said: {text}")

        except sr.UnknownValueError:
            st.write("Speak again please")
        except sr.RequestError:
            st.write("Speech Service down")

# # Source: https://github.com/olaDEN

