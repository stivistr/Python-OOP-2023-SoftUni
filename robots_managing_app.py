from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {
        'MainService': MainService,
        'SecondaryService': SecondaryService,
    }

    VALID_ROBOTS = {
        'MaleRobot': MaleRobot,
        'FemaleRobot': FemaleRobot,
    }

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        service = [s for s in self.services if s.name == name]

        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICES[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        robot = [d for d in self.robots if d.name == name]

        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(filter(lambda r: r.name == robot_name, self.robots))
        service = next(filter(lambda s: s.name == service_name, self.services))

        if robot.kind == 'FemaleRobot' and service.name != 'SecondaryService':
            return "Unsuitable service."

        if robot.kind == 'MaleRobot' and service.name != 'MainService':
            return "Unsuitable service."

        if service.capacity < robot.weight:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))
        robot = next(filter(lambda r: r.name == robot_name, service.robots))

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))

        if service:
            for robot in service.robots:
                robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))

        robots_price_in_service = 0
        if service:
            for robot in service.robots:
                robots_price_in_service += robot.price

        return f"The value of service {service_name} is {robots_price_in_service:.2f}."

    def __str__(self):
        robots_in_service = []
        for service in self.services:
            robots_in_service.append(service.details())

        return '\n'.join(robots_in_service)


main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))
print(main_app.add_robot('MaleRobot', 'Rob', 'SomeRobots', 200.11))
print(main_app.add_robot_to_service('Rob', 'ServiceTechnicalsWorld'))
print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))

print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))

print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))

print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))
