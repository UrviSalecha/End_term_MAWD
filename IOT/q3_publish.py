# Security Camera use OpenCV : Live video from camera and real time face detection
# Integrate MQTT alert message when face detected subscribe to the alert topic display alert in real time 

import cv2
import paho.mqtt.client as mqtt

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
cap = cv2.VideoCapture(0)


# Subscriber Side
def on_alert(client, userdata, msg):
    print('Alert!!', msg.payload.decode())

sub_client = mqtt.Client()
sub_client.on_message = on_alert
try:
    sub_client.connect('localhost', 1883, 60)
    sub_client.subscribe('face_detected')
    sub_client.loop_start()
except Exception as e:
    print('Subscriber connect error:', e)


# Publisher side
pub_client = mqtt.Client()
try:
    pub_client.connect('localhost', 1883, 60)
    pub_client.loop_start()
except Exception as e:
    print('Publisher connect error:', e)

payload = 'Face detected in camera feed'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        try:
            pub_client.publish('face_detected', payload)
        except Exception:
            pass

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

try:
    pub_client.loop_stop()
    pub_client.disconnect()
except Exception:
    pass

try:
    sub_client.loop_stop()
    sub_client.disconnect()
except Exception:
    pass

    
