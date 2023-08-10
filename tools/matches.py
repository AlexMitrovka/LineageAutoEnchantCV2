import cv2
from tools.windowcapture import WindowCapture
from time import time
import numpy as np
import pytesseract
from PIL import ImageGrab
from time import sleep
from settings import Settings
# зчитуємо вихідне зображення та шаблонне зображення

template = cv2.imread(Settings.source_chat)
screen = WindowCapture(Settings.window_name)
custom_oem_psm_config = r'--oem 2 --psm 6'
template_found = False
template_coordinates = None
# loop_time = time()
def VisionEnchante():
    global template_found, template_coordinates

    if not template_found:
        screenshot = screen.get_screenshot()
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        top_left = max_loc
        bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
        top_xy = screen.get_screen_position(top_left)
        bot_xy = screen.get_screen_position(bottom_right)
        img = np.array(ImageGrab.grab(bbox=(top_xy[0] + 18, top_xy[1] - 5, bot_xy[0] + 80, bot_xy[1] + 3)))
        ret, thresh = cv2.threshold(img, 200, 200, cv2.THRESH_BINARY_INV)
        cv2.imshow("Img", thresh)
        text = pytesseract.image_to_string(thresh, config=custom_oem_psm_config)
        str = text.strip().split()
        if str and str[0]:
            # Store the template coordinates
            template_found = True
            template_coordinates = (top_left, bottom_right)
            return str[0]
        else:
            return " "
    else:
        # Use the stored template coordinates
        top_left, bottom_right = template_coordinates
        top_xy = screen.get_screen_position(top_left)
        bot_xy = screen.get_screen_position(bottom_right)
        img = np.array(ImageGrab.grab(bbox=(top_xy[0] + 18, top_xy[1] - 5, bot_xy[0] + 80, bot_xy[1] + 3)))
        ret, thresh = cv2.threshold(img, 200, 200, cv2.THRESH_BINARY_INV)
        cv2.imshow("Img", thresh)
        text = pytesseract.image_to_string(thresh, config=custom_oem_psm_config)
        str = text.strip().split()
        if str and str[0]:
            return str[0]
        else:
            return " "

# text = VisionEnchante()
#
# print(text)