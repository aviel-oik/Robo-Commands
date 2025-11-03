import classes.robot
from abc import ABC, abstractmethod

class MovableMixin(classes.robot.Robot, ABC):
    def __init__(self, name, localisation):
        super().__init__(name)
        self.localisation = localisation

    @abstractmethod
    def move(self,x,y):
        pass
