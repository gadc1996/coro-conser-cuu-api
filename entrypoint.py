from django.core import management
from django.contrib.auth.models import User
import subprocess

def main():
    _migrate_database()
    _create_superuser()

def _migrate_database():
    management.call_command('migrate')

def _create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')

def _run_server():
    subprocess.call(['gunicorn', 'app.wsgi:application', '--bind', '0.0.0.0:8080'])

if __name__ == '__main__':
    main()