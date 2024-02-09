class User:
    def __init__(self, name: str, email: str, password: str, role: str) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def change_password(self, new_password: str) -> None:
        print(f"{self.name} is changed password {self.password} to {new_password}")


class AuthService:
    @staticmethod
    def register(user: User) -> None:
        print(f"{user.name} is registered with email {user.email} and password {user.password}")

    @staticmethod
    def login(user: User) -> None:
        print(f"{user.name} is logged in with email {user.email} and password {user.password}")

    @staticmethod
    def logout(user: User) -> None:
        print(f"{user.name} is logged out")


class EmailService:
    @staticmethod
    def send_email(user: User, subject: str, message: str, recipients: str) -> None:
        print(f"{user.name} is sent message {message} with {subject} to {recipients}")


class ReportService:
    @staticmethod
    def generate_report(user: User, data: str) -> None:
        print(f"{user.name} is generated report with data {data}")
