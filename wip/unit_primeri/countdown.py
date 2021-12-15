# use recursive function
import time


def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        time.sleep(1)
        countdown(x-1)


countdown(5)

n: int
for n in range(5):
    print(n)
    time.sleep(1)
