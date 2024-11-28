from time import sleep
from random import randint
def random_sleep(duration):
    # print("Duration is ", duration)
    duration=randint(max((duration*100)-30, 0), ((duration*100)+30))/100
    sleep(duration)
