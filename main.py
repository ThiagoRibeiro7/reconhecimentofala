import speech_recognition as sr

# - criar um "reconhecedor"
rec = sr.Recognizer()

# para escolher qual microfone vamos usar, rode:
# print(sr.Microphone().list_microphone_names())
with sr.Microphone(device_index=3) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode começar a falar:")

    # rec.pause_threshold = 1 # coloque isso se quiser que ele demore mais para entender que uma pausa é o fim do audio
    audio = rec.listen(mic)
try:
    # reconhece esse audio e traduz ele pra texto
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
except:
    print("Não consegui entender o áudio")
