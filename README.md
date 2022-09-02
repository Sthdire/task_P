# task_P

Api для работы с клиентской базой. Функции: добавление клиентов, рассылок, запуск рассылки, получение полной и детальной статистики по рассылкам. Осуществлена интеграция со внегним OpenAPI

Инструкция по запуску: перед использованием скрипта скачайте все пакеты из файла requirements.txt, затем зайдите в файл db_connect.py и измините значение переменной db_password на свой пароль от postgreSQL, перейдите в файл models.py и измените пароль в app.config['SQLALCHEMY_DATABASE_URI'] по форме 'postgresql://postgres:ВАШ_ПАРОЛЬ@localhost/t_db', для запуска используйте файл app.py, а для тестирования запустите папку tests при помощи pytests интерпретатора, также при локальном запуске сменити параметр host в db_connect.py в методе create_database и в сдеющим за ним экземпляре подключения con, а также в models.py на строчке app.config['SQLALCHEMY_DATABASE_URI']

Для просмотра документации по API перейдите в файл API_documentation.md наcтоящего репозитория.

Из дополнительных пунктов реализованы:

№1 - организовать тестирование написанного кода

№3 - подготовить docker-compose для запуска всех сервисов проекта одной командой
