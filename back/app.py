import requests
from flask import Flask
from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide
from flask_cors import CORS
import os
from Repositories import JsonProjectRepository, IProjectsRepository, \
    IUsersRepository, JsonUsersRepository, IReportsRepository, JsonReportsRepository

app = Flask(__name__)
CORS(app)


class Container(containers.DeclarativeContainer):

    project_repository = providers.Factory(JsonProjectRepository)
    user_repository = providers.Factory(JsonUsersRepository)
    report_repository = providers.Factory(JsonReportsRepository)


def send_message_in_telegram(chat_id: int, message: str):
    bot_token = '6128900927:AAF2c0dLwq2SHIJAhvPxhETzGwh8jjKyvqA'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(chat_id) \
                + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)

    return


@app.route('/grant_fields')
def grant_fields():
    with open('storage/mock_grant_fields.json', 'r') as file:
        data = file.read()
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )

    return response


@app.route('/alert_users_from_unfinished_projects')
@inject
def alert_users_from_unfinished_projects(
        project_repository: IProjectsRepository = Provide[Container.project_repository],
        user_repository: IUsersRepository = Provide[Container.user_repository]
    ):
    users = project_repository.get_users_from_unfinished_projects()
    for user in users:
        chat_id = user_repository.get_user_chat_id_by_id(user)
        send_message_in_telegram(chat_id, "Вы не закончили оформлять проект")

    return ""


@app.route('/alert_users_from_projects_without_event')
@inject
def alert_users_from_projects_without_event(
        project_repository: IProjectsRepository = Provide[Container.project_repository],
        user_repository: IUsersRepository = Provide[Container.user_repository]
    ):
    users = project_repository.get_users_from_projects_without_event()
    for user in users:
        chat_id = user_repository.get_user_chat_id_by_id(user)
        send_message_in_telegram(chat_id, "Вы еще не подали ваш проект ни на одно мероприятие")

    return ""


@app.route('/alert_users_with_report_deadline')
@inject
def alert_users_with_report_deadline(
        project_repository: IProjectsRepository = Provide[Container.project_repository],
        user_repository: IUsersRepository = Provide[Container.user_repository],
        report_repository: IReportsRepository = Provide[Container.report_repository],
    ):
    reports = report_repository.get_reports_with_deadline(2)
    print(reports, flush=True)
    for report in reports:
        user = project_repository.get_user_from_project_by_report_id(report)
        chat_id = user_repository.get_user_chat_id_by_id(user)
        send_message_in_telegram(chat_id, "Дедлайн по отчету все ближе")

    return ""


@app.route('/alert_users_from_changed_project_status')
@inject
def alert_users_from_changed_project_status(
        project_repository: IProjectsRepository = Provide[Container.project_repository],
        user_repository: IUsersRepository = Provide[Container.user_repository]
    ):
    users = project_repository.get_users_from_changed_project_status()
    for user in users:
        chat_id = user_repository.get_user_chat_id_by_id(user)
        send_message_in_telegram(chat_id, "Статус вашей заявки изменился")

    return ""


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)