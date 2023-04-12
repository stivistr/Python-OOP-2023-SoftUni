from project.services.base_service import BaseService


class MainService(BaseService):
    MAIN_SERVICE_CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, self.MAIN_SERVICE_CAPACITY)

    def details(self):
        if not self.robots:
            return f"{self.name} Main Service:\nRobots: none"

        return f"{self.name} Main Service:\nRobots: {' '.join(str(r.name) for r in self.robots)}"

