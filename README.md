Прилжение-библиотека на Django.

1. Создайт виртуальное окружение: python3 -m venv env
2. Активируйте виртуальное окружение: source env/bin/activate
3. Чтобы установить все требуемые библиотеки python в новом окружении выполните команду: pip install -r requirements.txt
   
   Если у вас macOS до выполнения команды pip install -r requirements.txt выполните команду:       
   env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2==2.8.4 
   Для предотвращения появления ошибки (error: command 'gcc' failed with exit status 1.) при установке зависимостей.
   
4. Чтбы запустить сервер введите команду: python manage.py runserver

Для входа в администравтивную панель проекта создайте суперпользователя при помощи команды: python manage.py createsuperuser

Список роутов:

admin/ - панель администратора;

index/ - таблица книг в билиотеке;

publishers/ - вывод списка издательств и их книг;

author/create/ - создать нового автора (формы);

author/create_many/ - создать несколько авторов за один раз (формы);

authors/ - список авторов, книги которых есть в библиотеке;

author_book/create_many/ - добавить несколько авторов и несколько книг одновременно (формы);

friends/ - вывод списка друзей и книг, взятых ими из библиотеки.
