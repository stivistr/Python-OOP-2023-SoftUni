from project.services.base_service import BaseService


class SecondaryService(BaseService):
    SECONDARY_SERVICE_CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.SECONDARY_SERVICE_CAPACITY)

    def details(self):
        if not self.robots:
            return f"{self.name} Secondary Service:\nRobots: none"

        return f"{self.name} Secondary Service:\nRobots: {' '.join(str(r.name) for r in self.robots)}"

