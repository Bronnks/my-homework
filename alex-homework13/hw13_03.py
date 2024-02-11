from abc import ABC, abstractmethod


class Bird(ABC):
    def __init__(self, name: str, wingspan: float) -> None:
        self.name = name
        self.wingspan = wingspan


class FlyingBird(Bird):
    @abstractmethod
    def fly(self) -> None:
        pass


class Eagle(FlyingBird):
    def fly(self) -> None:
        print(f"{self.name} is flying with wingspan {self.wingspan}")


class FlightlessBird(Bird):
    @abstractmethod
    def move(self) -> None:
        pass


class Penguin(FlightlessBird):
    def move(self) -> None:
        print(f"{self.name} can't fly, but can swim")


class Ostrich(FlightlessBird):
    def move(self) -> None:
        print(f"{self.name} can't fly, but can run")
