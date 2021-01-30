import numpy as np
from PIL import ImageGrab
import cv2
import time
from others.key import PressKey, ReleaseKey, SPACE

def jumper():
    for i in list(range(4)) [::-1]:
        print(i+1)
    time.sleep(1)

    while True:
        print('jump')
        PressKey(SPACE)
        time.sleep(0.1)
        ReleaseKey(SPACE)
        time.sleep(2)

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=150, threshold2=250)
    return processed_img

def screen_record():
    last_time = time.time()
    while True:
        screen =  np.array(ImageGrab.grab(bbox=(0,285,1280,1005)))
        new_screen = process_img(screen)
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window2',new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

#screen_record()
jumper()
