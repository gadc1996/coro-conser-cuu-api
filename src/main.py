import subprocess


def runserver():
    subprocess.run(["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8080", "core.wsgi:application"], check=True)

def migrate():
    subprocess.run(["poetry", "run", "python", "manage.py", "migrate"], check=True)
    
def collectstatic():
    subprocess.run(["poetry", "run", "python", "manage.py", "collectstatic", "--noinput"], check=True)
    
if __name__ == "__main__":
    migrate()
    collectstatic()
    runserver() 