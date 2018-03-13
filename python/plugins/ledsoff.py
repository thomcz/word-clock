class LedsOff():

    def run(self):
        self.strip.resetLeds()

    def __init__(self, strip):
        self.strip = strip
