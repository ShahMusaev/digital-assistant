from .IProjectsRepository import IProjectsRepository
import json


class JsonProjectRepository(IProjectsRepository):

    def get_users_from_unfinished_projects(self) -> list:
        with open('storage/mock_projects.json', 'r') as file:
            data = json.load(file)

        res = []
        for item in data:
            if not item["is_finished"]:
                res += [item["user_id"]]

        return res

    def get_users_from_projects_without_event(self) -> list:
        with open('storage/mock_projects.json', 'r') as file:
            data = json.load(file)

        res = []
        for item in data:
            if item["event_id"] is None:
                res += [item["user_id"]]

        return res

    def get_user_from_project_by_report_id(self, report_id) -> int:
        with open('storage/mock_projects.json', 'r') as file:
            data = json.load(file)

        res = []
        for item in data:
            if item["report_id"] == "report_id":
                return item["user_id"]

    def get_users_from_changed_project_status(self) -> list:
        with open('storage/mock_projects.json', 'r') as file:
            data = json.load(file)

        res = []
        for item in data:
            if item["status"] == "changed":
                res += [item["user_id"]]

        return res
