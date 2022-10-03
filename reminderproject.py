import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "**Please Drink Water Now!!",
            message ="drinking water is good for Health SIR",

            timeout= 10
            )

        #	time.sleep(6)
        time.sleep(13)
