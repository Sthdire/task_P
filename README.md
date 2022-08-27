# task_P

Инструкция по запуску: перед использованием скрипта скачайте все пакеты из файла requirements.txt, затем зайдите в файл db_connect.py и измините значение переменной db_password на свой пароль от postgreSQL, перейдите в файл models.py и измените пароль в app.config['SQLALCHEMY_DATABASE_URI'] по форме 'postgresql://postgres:ВАШ_ПАРОЛЬ@localhost/t_db', для запуска используйте файл app.py, а для тестирования запустите папку tests при помощи pytests интерпритатора.

Для просмотра документации по API перейдите в файл API_documentation.md начтоящего репозитория.
