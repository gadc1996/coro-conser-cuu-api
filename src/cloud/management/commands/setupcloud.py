import subprocess
import secrets
from typing import Any

from django.conf import settings
from django.core.management.base import BaseCommand
from termcolor import cprint

from utils.env import EnvFile


class Command(BaseCommand):
    help = "Setup AWS Elastic Beanstalk application and environment with database"

    def handle(self, *args: Any, **options: Any) -> str | None:
        self._setup_app()
        self._setup_enviroment()
        return None

    def _setup_app(self) -> None:
        command = [
            "eb",
            "init",
            "--platform",
            settings.ENV("AWS_PLATFORM"),
            "--region",
            settings.ENV("AWS_REGION"),
            settings.ENV("APP_NAME"),
        ]

        try:
            subprocess.run(
                command,
                check=True,
            )
        except subprocess.CalledProcessError as e:
            cprint(
                f"Failed to setup AWS Elastic Beanstalk application, Error: {e}", "red"
            )
        else:
            cprint("Setup AWS Elastic Beanstalk application", "green")

    def _setup_enviroment(self) -> None:
        env_file = EnvFile(settings.ENV("CLOUD_ENV_FILE"))
        command = [
            "eb",
            "create",
            f"{settings.ENV('APP_NAME')}-dev",
            "-im",
            "1",
            "-ix",
            "1",
            "--cname",
            f"{settings.ENV('APP_NAME')}-dev",
            "--envvars",
            env_file.as_string(),
            "--database",
            "--database.engine",
            "mysql",
            "--database.username",
            "ebroot",
            "--database.password",
            secrets.token_urlsafe(16),
            "--database.size",
            "5",
            "--database.instance",
            "db.t2.micro",
        ]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            cprint(
                f"Failed to setup AWS Elastic Beanstalk environment, Error: {e}", "red"
            )
        else:
            cprint("Setup AWS Elastic Beanstalk environment", "green")
