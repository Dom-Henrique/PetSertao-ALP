import cv2, os

def validacao():
    webcam = cv2.VideoCapture(0) # Importa o modo de captura

    if webcam.isOpened():
        validacao, frame = webcam.read()  # Lê a câmera. Nesse caso, é recomendado duas variáveis para evitar erros.
        while validacao:
            validacao, frame = webcam.read()
            cv2.imshow("Validação de usuários", frame) # Apresenta a imagem ao usuário
            key = cv2.waitKey(5) # Atrasp de 5 segundos (altíssimo disparo)
            if key == 27: # Key 27 é a tecla ESC
                break
        os.mkdir('rostos_base')
        cv2.imwrite('rostos_base/Foto_Validacao.png', frame) # Salva a imagem
        
    webcam.release()
    cv2.destroyAllWindows()
    
validacao()