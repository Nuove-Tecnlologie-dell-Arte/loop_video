import cv2

def mammt(nume):
    # Carica il video
    filename=str(nume)
    cap = cv2.VideoCapture('vid/'+filename+'.mp4')
    # Ottieni le dimensioni del video
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Crea la finestra in full screen
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Ciclo principale
    while cap.isOpened():
        # Leggi un frame dal video
        ret, frame = cap.read()

        # Se il frame è stato letto correttamente
        if ret:
            # Ridimensiona il frame per adattarlo alla finestra
            frame = cv2.resize(frame, (width, height))

            # Mostra il frame nella finestra
            cv2.imshow('Video', frame)

            # Se viene premuto il tasto ESC, esci dal ciclo
            if cv2.waitKey(25) & 0xFF == 27:
                break
        else:
            break

    # Rilascia le risorse
    cap.release()
    cv2.destroyAllWindows()