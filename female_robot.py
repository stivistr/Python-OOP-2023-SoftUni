from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    FEMALE_WEIGHT = 7

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.FEMALE_WEIGHT)

    def eating(self):
        self.FEMALE_WEIGHT += 1

