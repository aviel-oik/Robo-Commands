import classes.speakableMixin

class GuardRobot(classes.speakableMixin.SpeakableMixin):
    def speak(self, message):
        print(f"{self.name} Speak and say {message}")