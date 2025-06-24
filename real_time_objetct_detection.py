import numpy as np
import cv2
import imutils
from imutils.video import FPS
import time
from base64 import b64encode

# construct the argument parse and parse the arguments
video_source = "./video/pessoavideo.mp4"
prototxt_path = "./MobileNetSSD_deploy.prototxt.txt"
model_path = "./MobileNetSSD_deploy.caffemodel"
confidence_threshold = 0.2

itemIdentificado = "person"

camera = cv2.VideoCapture(video_source)

# inicializar a lista de rótulos de classe que o MobileNet SSD foi treinado
# para detectar e, em seguida, gerar um conjunto de cores de caixa delimitadora
# para cada classe
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# carregue nosso modelo serializado do disco
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

fps = FPS().start()
while True:
    # pega o atual frame
    (grabbed, image) = camera.read()

    try:
        # redimensiona o quadro para 400 pixels de largura
        image = imutils.resize(image, width=600)

        # carregue a imagem de entrada e construa um blob de entrada para a imagem
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)),
                                     0.007843, (300, 300), 127.5)

        # passe o blob pela rede e obtenha as detecções e previsões
        net.setInput(blob)
        detections = net.forward()

        # percorrer as detecções
        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            idx = int(detections[0, 0, i, 1])

            if confidence > confidence_threshold and CLASSES[idx] == itemIdentificado:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
                cv2.rectangle(image, (startX, startY), (endX, endY), COLORS[idx], 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(image, label, (startX, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

        # Mostra a saída da imagem
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        fps.update()
    except:
        print("Vídeo acabou ou não foi possível exibi-lo!")
        break

# libera o uso da camera e fecha a janela aberta
fps.stop()
print("FPS = {}".format(fps.fps()))
camera.release()
cv2.destroyAllWindows()
