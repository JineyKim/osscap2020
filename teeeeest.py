from matrix import *
import LED_display as LMD
import threading

def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

LED_init()

LMD.set_pixel(1,1,1)
LMD.set_pixel(30,24,7)
