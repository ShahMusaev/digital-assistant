from abc import ABC, abstractmethod


class IProjectsRepository(ABC):

    @abstractmethod
    def get_users_from_unfinished_projects(self) -> list:
        pass

    @abstractmethod
    def get_users_from_projects_without_event(self) -> list:
        pass

    @abstractmethod
    def get_user_from_project_by_report_id(self, report_id) -> int:
        pass

    @abstractmethod
    def get_users_from_changed_project_status(self) -> list:
        pass
