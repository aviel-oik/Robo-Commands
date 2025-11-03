import classes.movableMixin
import classes.speakableMixin

class DeliveryRobot(classes.movableMixin.MovableMixin, classes.speakableMixin.SpeakableMixin):

    def speak(self, message):
        print(f"{self.name} Speak and say {message}")

    def move(self,x,y):
        self.localisation[0] = x
        self.localisation[1] = y

