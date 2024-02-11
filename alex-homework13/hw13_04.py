from abc import ABC


class Phone(ABC):
    def __init__(self, model: str, number: int) -> None:
        self.model = model
        self.number = number


class CallPhone(Phone):
    def call(self, other_number: int) -> None:
        print(f"Calling {other_number} from {self.number}")


class MessagePhone(Phone):
    def send_message(self, other_number: int, text: str) -> None:
        print(f"Sending '{text}' to {other_number} from {self.number}")


class PhotoPhone(Phone):
    def take_photo(self) -> None:
        print(f"Taking a photo with {self.model}")


class GamePhone(Phone):
    def play_game(self, game: str) -> None:
        print(f"Playing {game} on {self.model}")


class BasicPhone(CallPhone, MessagePhone):
    pass


class CameraPhone(CallPhone, MessagePhone, PhotoPhone):
    pass


class SmartPhone(CallPhone, MessagePhone, PhotoPhone, GamePhone):
    pass
