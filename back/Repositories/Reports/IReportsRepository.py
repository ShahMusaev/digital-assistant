from abc import ABC, abstractmethod


class IReportsRepository(ABC):

    @abstractmethod
    def get_reports_with_deadline(self, days_to_deadline: int) -> list:
        pass