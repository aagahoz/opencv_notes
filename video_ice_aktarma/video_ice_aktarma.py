import cv2
import time

# video ismi 

video_name = "MOT17-04-DPM.mp4"

# video içe aktar capture
cap = cv2.VideoCapture(video_name)

print("Genislik:   ", cap.get(3))
print("Yükseklik:   ", cap.get(4))

if cap.isOpened() == False:
    print("Video Dosyası Açılamadı...")
        

while True:
    
    ret, frame = cap.read()
    
    if ret == True:
        
        time.sleep(0.01) # bunu yapmazsak çok hızlı akar
        
        cv2.imshow("Video", frame)
        
    else:
        break
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    
cap.release()  # stop capture
cv2.destroyAllWindows()