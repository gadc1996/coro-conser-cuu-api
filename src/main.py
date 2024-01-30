import subprocess


def runserver():
    subprocess.run(
        [
            "gunicorn",
            "--bind",
            "0.0.0.0:8080",
            "core.wsgi:application",
        ],
        check=True,
    )


def migrate():
    subprocess.run(["python", "manage.py", "migrate"], check=True)


def collectstatic():
    subprocess.run(
        ["python", "manage.py", "collectstatic", "--noinput"],
        check=True,
    )


if __name__ == "__main__":
    migrate()
    collectstatic()
    runserver()
