import numpy as np
import cv2
import time
from grabscreen import grab_screen
from key import PressKey, ReleaseKey, SPACE


def jumper():
    for i in list(range(4))[::-1]:
        print(i + 1)
    time.sleep(1)

    while True:
        print('jump')
        PressKey(SPACE)
        time.sleep(2)
        ReleaseKey(SPACE)
        time.sleep(2)


def process_img(original_image):
    processed_img = cv2.resize(original_image, (0, 0), fx=0.5, fy=0.5)
    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_RGB2GRAY)
    # processed_img = cv2.Canny(processed_img, threshold1=160, threshold2=300)
    processed_img = cv2.GaussianBlur(processed_img, (15, 15), 0)
    return processed_img


def run():
    last_time = time.time()
    while True:
        screen = grab_screen(region=(1, 285, 1276, 1000))
        new_screen = process_img(screen)
        im = np.array(new_screen)
        print(im)
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow('window2', new_screen)
        # cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


run()
# jumper()
