import json

from .IUsersRepository import IUsersRepository


class JsonUsersRepository(IUsersRepository):

    def get_user_chat_id_by_id(self, user_id: int) -> int:
        with open('storage/mock_users.json', 'r') as file:
            data = json.load(file)

        res = []
        for item in data:
            if item["id"] == user_id:
                return item["chat_tg_id"]
