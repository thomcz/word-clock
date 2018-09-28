from subprocess import call
from strip.ledstrip import LedStrip


if __name__== "__main__":
    LedStrip().resetLeds()
    call("sudo shutdown -h 0", shell = True)
