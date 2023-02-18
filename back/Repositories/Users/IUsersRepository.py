from abc import ABC, abstractmethod


class IUsersRepository(ABC):

    @abstractmethod
    def get_user_chat_id_by_id(self, user_id: int) -> int:
        pass
