import json
import datetime

from .IReportsRepository import IReportsRepository


class JsonReportsRepository(IReportsRepository):

    def get_reports_with_deadline(self, days_to_deadline: int) -> list:
        with open('storage/mock_reports.json', 'r') as file:
            data = json.load(file)
        res = []
        for item in data:
            deadline = datetime.datetime.strptime(item["deadline"], '%Y-%m-%d %H:%M')
            now = datetime.datetime.now()

            if now < deadline < now + datetime.timedelta(days=days_to_deadline):
                res += [item["id"]]

        return res
