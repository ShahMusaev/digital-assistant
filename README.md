### Функциональность
1. Помошь при навигации по веб ресурсу - https://grants.myrosmol.ru/
2. Помощь при составлении заявки
3. Голосовое управление
4. Уведомление пользователей через телеграмм о событиях:
    * Не закончено оформление проекта
    * Проект не прикреплен к мероприятию
    * Изменения статуса заявки
    * Приближается дедлайн отчетности

### Особенность проекта
1. Автомат состояний для навигации по сайту / форме заявки.
2. Фронтенд реализован одним js файлом через иньекцию на сайт (см. инструкцию ниже).
3. Универифицированная работа с автоматом состояния, что позволяет легко дополнять пользовательский опыт.
4. Универифицированный интерфейс для Репозиториев на бэкенде. Позволяет абстрагировать способ хранения данных от главной функциональности - уведомления. Что позволит ускорить интеграцию предложенного подхода.
5. Возможность заполнение полей в форме через голосовое управление.

### Основной стек
1. HTML, CSS, JavaScript
2. Python

### Демо
https://drive.google.com/drive/folders/1COIU6I4XYeJCAiAlJrhd3l5VOGjP4VGA?usp=share_link

## Установка (бэкенд)
1. `cd back`
2. `docker image build -t ros_grant_backend`
2. `docker run -p 5000:5000  ros_grant_backend`

## Установка (фронтенд)
1. Открыть в Chrome панель разработчика (DevTools)
2. Перейти на вкладку Sources
3. Слева выбрать подраздел Overrides
4. Выбрать локальную папку для хранения измененных файлов
5. Под адресной строкой появится запрос на предоставление доступа к папке - нажимаем кнопку "Разрешить"
6. Скопировать скрипт из папки front в папку выбранную на 4 шаге
