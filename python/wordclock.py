import time 
import datetime

from neopixel import *

#from array import array

# LED strip configuration:
LED_COUNT      = 110      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

ES_IST = [9,10,30,49,50]
EIN = [24,35,44]
EINS = EIN + [55]
ZWEI = [4,15,24,35]
DREI = [16,23,36,43]
VIER = [77,82,97,102]
FUENF = [76,83,96,103]
SECHS = [19,20,39,40,59]
SIEBEN = [55,64,75,84,95,104]
ACHT = [18,21,38,41]
NEUN = [37,42,57,62]
ZEHN = [58,61,78,81]
ELF = [2,17,22]
ZWOELF = [54,65,74,85,94]
STUNDE = [EINS, ZWEI, DREI, VIER, FUENF, SECHS, SIEBEN, ACHT, NEUN, ZEHN, ELF, ZWOELF]

#X nach/vor
NACH = [26,33,46,53]
VOR = [66,73,86]

FUENF_MINUTE = [70,89,90,109]
ZEHN_MINUTE = [8,11,28,31]
VIERTEL = [47,52,67,72,87,92,107]
ZWANZIG = [48,51,68,71,88,91,108]
HALB = [5,14,25,34]


#X nach
FUENF_NACH = FUENF_MINUTE + NACH
ZEHN_NACH = ZEHN_MINUTE + NACH
VIERTEL_NACH = VIERTEL + NACH
ZWANZIG_NACH = ZWANZIG + NACH
FUENF_NACH_HALB = FUENF_MINUTE + NACH + HALB

#X vor
FUENF_VOR = FUENF_MINUTE + VOR
ZEHN_VOR = ZEHN_MINUTE + VOR
VIERTEL_VOR = VIERTEL + VOR
ZWANZIG_VOR = ZWANZIG + VOR
FUENF_VOR_HALB = FUENF_MINUTE + VOR + HALB

UHR = [80,99,100]

def setClock(strip, color, ledList):
        for led in ledList:
                strip.setPixelColor(led, color)
                strip.show()

def resetLeds():
	for led in range(strip.numPixels()):
		strip.setPixelColor(led, 0)
		strip.show()

if __name__ == '__main__':
        # Process arguments
        #opt_parse()

        # Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other functions).
        strip.begin()
        #print ('Press Ctrl-C to quit.')
        while True:
		resetLeds()
                color = Color(255,255,255)
                now = datetime.datetime.now()
		print(now)
                minute = now.minute
                hour = now.hour

                if (minute < 5):
                        setClock(strip, color, ES_IST + STUNDE[hour%12] + UHR)
                elif (minute < 10):
                        setClock(strip, color, ES_IST + FUENF_NACH + STUNDE[hour%12])
                elif (minute < 15):
                        setClock(strip, color, ES_IST + ZEHN_NACH + STUNDE[hour%12])
                elif (minute < 20):
                        setClock(strip, color, ES_IST + VIERTEL_NACH + STUNDE[hour%12])
		elif (minute < 25):
                        setClock(strip, color, ES_IST + ZWANZIG_NACH + STUNDE[hour%12])
                elif (minute < 30):
                        setClock(strip, color, ES_IST + FUENF_VOR_HALB + STUNDE[hour%12])
                elif (minute < 35):
                        setClock(strip, color, ES_IST + HALB + STUNDE[(hour+1)%12])
                elif (minute < 40):
                        setClock(strip, color, ES_IST + FUENF_NACH_HALB + STUNDE[(hour+1)%12])
                elif (minute < 45):
                        setClock(strip, color, ES_IST + ZWANZIG_VOR + STUNDE[(hour+1)%12])
                elif (minute < 50):
                        setClock(strip, color, ES_IST + VIERTEL_VOR + STUNDE[(hour+1)%12])
                elif (minute < 55):
                        setClock(strip, color, ES_IST + ZEHN_VOR + STUNDE[(hour+1)%12])
                elif (minute < 60):
                        setClock(strip, color, ES_IST + FUENF_VOR + STUNDE[(hour+1)%12])
		time.sleep(30)

                #setClock(strip, Color(255, 0, 0), ES_IST + VIERTEL_VOR + EIN)  # Red wipe
                #colorWipe(strip, Color(0, 255, 0))  # Blue wipe
                #colorWipe(strip, Color(0, 0, 255))  # Green wipe

 
