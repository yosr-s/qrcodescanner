import cv2
from pyzbar.pyzbar import decode
import time
from datetime import datetime
import requests

cap=cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
used_codes=[]

date = datetime.now().strftime("%Y-%m-%d")
time2 = datetime.now().strftime("%H:%M:%S")
time1=time2[0:2]

camera=True
while camera==True:
    success,frame=cap.read()
    for code in decode(frame):
        if code.data.decode('utf-8') not in used_codes:
            print('approved! you can enter!')
            var=code.data.decode('utf-8')
            print(var)
            used_codes.append(code.data.decode('utf-8'))
            x=var.split('-')
            cin=str(x[0])
            idd=str(x[1])
            nom=str(x[2])
            prenom=str(x[3])
            time.sleep(5)

            payload = {'cin': cin, 'nom': nom, 'prenom': prenom, 'time': time2, 'date': date, 'time1': time1,'idd':idd}
            r1 = requests.get('http://localhost/projet-se/templates/api-view.php', params=payload)
            url = r1.url
            print(url)
            print(r1.text)



        elif code.data.decode('utf-8') in used_codes:
            print('sorry! used code!')
            time.sleep(5)



    cv2.imshow('testing-code-scan',frame)
    cv2.waitKey(1)






