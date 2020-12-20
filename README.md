Перед установкой проекта обновите Python3 до Python 3.9.1
Если ваша операционная система Linux
1. Откройте терминал
2. Перейдите в директорию проекта
3. Выполните sh python3.9.1_install
4. Следуйте дальнейшим указаниям в терминале

Если ваша операционная система Windows
1. Скачайте файл с https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe
2. Запустите установку Python3.9.1

Инструкция по установке проекта
1. git clone https://gitlab.informatics.ru/SOmegaS/simple-votings-chernovik.git
2. Открыть проект в PyCharm
3. Нажать в уведомлении (справа снизу) Configure Interpreter
4. Создать новое виртуальное окружение на основе установленного Python3.9.1
   1. Ввести в терминал which python3.9
   2. Указать в поле Base interpreter полученный путь к python3
5. Tools -> Sync Python Requirements -> Strong Equality -> OK
6. Add Configuration -> Указать путь к manage.py -> Параметры: runserver -> OK

Проект выполнен как черновик основной работы.

Created by proms101
