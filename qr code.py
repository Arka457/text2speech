import cv2
from pyzbar.pyzbar import decode
import time

cam = cv2.VideoCapture(0)
cam.set(3, 640)  # Set the width
cam.set(4, 480)  # Set the height

while True:
    success, frame = cam.read()

    if not success:
        continue

    for qr_code in decode(frame):
        qr_data = qr_code.data.decode('utf-8')
        print("QR Code Type: ", qr_code.type)
        print("QR Code Data: ", qr_data)
        time.sleep(6)

    cv2.imshow("Our_QR_code_scanner", frame)
    
    key = cv2.waitKey(1)  # Change to cv2.waitKey(0) for an indefinite wait
    if key == 27:  # Press 'Esc' to exit (27 is the ASCII code for 'Esc')
        break

cam.release()
cv2.destroyAllWindows()