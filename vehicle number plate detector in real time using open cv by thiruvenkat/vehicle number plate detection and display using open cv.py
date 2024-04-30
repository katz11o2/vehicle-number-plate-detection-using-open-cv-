import cv2

##########################################
nplatecascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
frameheight = 480
framewidth = 640
minarea = 200
###########################################
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frameheight)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, framewidth)
cap.set(cv2.CAP_PROP_FPS, 30)

if not cap.isOpened():
    print("error in opening your camera thiru")
    exit()

while True:
    sucess, img = cap.read()

    if not sucess:
        print("error again my friend")
        break

    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberplates = nplatecascade.detectMultiScale(imggray, 1.4, 4)

    for (x, y, w, h) in numberplates:
        area = w * h
        if area > minarea:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(img, "Detected", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.4, (0, 0, 250), 2)
            img_roi = img[y:y+h, x:x+w]  # Corrected indexing
            cv2.imshow("roi", img_roi)

    cv2.imshow("result", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
