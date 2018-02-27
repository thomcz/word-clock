from strip.ledstrip import LedStrip

class LedsOff():

    def run(self):
        self.strip.resetLeds()

    def __init__(self):
        self.strip = LedStrip()
            
if __name__ == '__main__':
    LedsOff().run()
