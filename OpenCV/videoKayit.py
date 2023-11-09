import cv2

camera = cv2.VideoCapture(0)

width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
heigth = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width,heigth)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
writter = cv2.VideoWriter("Kayit.mp4",fourcc,20,(width,heigth))

while True:
    ret,frame = camera.read()
    writter.write(frame)
    cv2.imshow("Kayit videosu",frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

camera.release()
writter.release()
cv2.destroyAllWindows()