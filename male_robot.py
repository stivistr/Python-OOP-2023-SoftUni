from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    MALE_WEIGHT = 9

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.MALE_WEIGHT)

    def eating(self):
        self.MALE_WEIGHT += 3
