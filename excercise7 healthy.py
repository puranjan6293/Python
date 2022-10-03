#Excercise7- Healthy programer

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg},{datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_excercise = time()

    watersecs = int(input("for water\n"))
    exsecs = int(input("for excercise\n"))
    eyesecs = int(input("for eyes\n"))
    while True:
        if time()-init_water>watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alaram.")
            musiconloop('water.mp3','drank')
            init_water=time()
            log_now("drank water at")

        if time()-init_eyes>eyesecs:
            print("Eye excercise time. Enter 'doneeyes' to stop the alaram.")
            musiconloop('eyes.mp3','doneeyes')
            init_eyes=time()
            log_now("eyes relaxed at")

        if time()-init_excercise>exsecs:
            print("physical activity time. Enter 'donephy' to stop the alaram.")
            musiconloop('phy.mp3','donephy')
            init_excercise=time()
            log_now("physical activity done at")



