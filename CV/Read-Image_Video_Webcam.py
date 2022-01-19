import cv2 as cv

def imgshow(imgname="cutegirl.jpg",consolename="Picture"):
    img=cv.imread(f"{imgname}")
    cv.imshow(f"{consolename}",img)
    cv.waitKey(0)
# waitkey: độ delay đơn vị milisecond (kiểu 1 khung hình trong bao nhiêu đó giây)
# nếu 0: vô hạn
################################################## Đọc Image ###################################################

#success: đẩy ra biến true or false(thực hiện được ko)
#image: đẩy cái hình

def videoshow(videoname="video.mp4",consolename="Video",fps=60,breakkey='q'):
    video=cv.VideoCapture(f"{videoname}")
    mspf=int(round(1000/fps))
    while True:
        success, image= video.read()
        cv.imshow(f"{consolename}",image)
        if cv.waitKey(mspf) and 0xFF==ord(f'{breakkey}'):
            break

################################################## Show video ##################################################

def webcamshow(width=640,height=480,brightness=100,consolename="Webcam",fps=60,breakkey='q'):
    wcam= cv.VideoCapture(0)#0 là mặc định cho webcam
    wcam.set(3,width) #id số 3 là width(rộng)
    wcam.set(4,height) #id số 4 là height(cao)
    wcam.set(10,brightness) #id 10 là độ sáng(brightness)
    mspf=int(round(1000/fps))
    while True:
        success, image= wcam.read()
        cv.imshow(f"{consolename}",image)
        if cv.waitKey(mspf) and 0xFF==ord(f'{breakkey}'):
            break

################################################### Web cam #####################################################
if __name__=="__main__":
    pass