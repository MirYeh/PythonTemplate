from template.models.user import User


class UserService:

    @staticmethod
    def greet(user: User) -> str:
        return f'Hey {user.name.title()}!'
