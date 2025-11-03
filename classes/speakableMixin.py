import classes.robot
from abc import ABC, abstractmethod

class SpeakableMixin(classes.robot.Robot, ABC):

    @abstractmethod
    def speak(self, message):
        pass
