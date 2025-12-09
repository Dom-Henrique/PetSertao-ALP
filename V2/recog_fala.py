import speech_recognition as sr

def reconhecimento_vocal(dados_usuario, index):
    reconhecer_voz = sr.Recognizer() # Chama uma biblioteca para ler o áudio

    # Para evitar que o microfone fique em looping
    with sr.Microphone() as mic:
        reconhecer_voz.adjust_for_ambient_noise(mic) # Ajusta o ruído para não atrapalhar na captação
        print('RECONHECENDO VOZ...')
        voz_usuario = reconhecer_voz.listen(mic) # Leitura do áudio
        fala_transcrita = reconhecer_voz.recognize_google(voz_usuario, language='pt-BR')
        print(fala_transcrita)
        if dados_usuario['ID'][index] == fala_transcrita:
            return True
        else:
            quit()