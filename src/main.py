import subprocess


if __name__ == "__main__":
    subprocess.run(["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8080", "core.wsgi:application"], check=True)
    