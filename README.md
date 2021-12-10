<a href="https://ya-llegue-django.herokuapp.com/login/" target="_blank" ># ya-llegue</a>
usuario de prueba
usuario: ana
contraseña: D12345678,

Clona el repositorio o descargalo como zip.
git clone https://github.com/anarkopin/ya-llegue.git

Crea un ambiente virtual
python -m virtuaenv env

Instala las dependencias/librerias en requirements.txt
pip install -r requirements.txt

Ejecuta las migraciones.
python manage.py makemigrations python manage.py migrate

Crea un superusuario.
python manage.py createsuperuser

Corre el servidor.
python manage.py runserver
