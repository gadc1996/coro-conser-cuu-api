import subprocess
from django.contrib.auth.models import User
from django.conf import settings


def runserver():
    subprocess.run(
        [
            "poetry",
            "run",
            "gunicorn",
            "--bind",
            "0.0.0.0:8080",
            "core.wsgi:application",
        ],
        check=True,
    )


def migrate():
    subprocess.run(["poetry", "run", "python", "manage.py", "migrate"], check=True)


def collectstatic():
    subprocess.run(
        ["poetry", "run", "python", "manage.py", "collectstatic", "--noinput"],
        check=True,
    )


def create_superuser():
    if not User.objects.filter(
        username=f"{settings.DJANGO_SUPERUSER_USERNAME}"
    ).exists():
        User.objects.create_superuser(
            f"{settings.DJANGO_SUPERUSER_USERNAME}",
            f"{settings.DJANGO_SUPERUSER_EMAIL}",
            f"{settings.DJANGO_SUPERUSER_PASSWORD}",
        )


if __name__ == "__main__":
    migrate()
    collectstatic()
    create_superuser()
    runserver()
