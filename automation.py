import cv2
import dropbox
import time
import random

startTime = time.time()

def takeSnapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while result:
        ret,frame = videoCaptureObject.read()
        imageName = 'image' + str(number) + '.png'
        cv2.imwrite(imageName, frame)
        startTime = time.time()
        result = False
    
    return imageName
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(imageName):
    accessToken = 'sl.BHoKeFuhqKA3CI8YQ3Hb2MTB7dH6VVQFdup-jwybLhuv0HvlPVh4EdDSKs88wscoKEGRR77iCSvQqIAZyfw1w8PtjXyzjhUF1Ht70Ho-MiTrDd3CcJSJzs2EAwdUbtlAhd_anQo'
    file_from = imageName
    file_to = f'/text_dropbox/{imageName}' 
    dbx = dropbox.Dropbox(accessToken)
    
    with open(file_from, 'rb')as f:
        dbx.files_upload(f.read(),file_to)

while True:
    if time.time() - startTime >= 5:
        name = takeSnapshot()
        uploadFile(name)