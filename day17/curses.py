

from time import sleep 

def gotoxy(x,y):
    print ("%c[%d;%df" % (0x1B, y, x), end='')


for x in range(10):
    gotoxy(5, 5)
    print(f"{x} is a dork")
    sleep(1)

    