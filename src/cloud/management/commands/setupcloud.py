import environ
import sys
import subprocess
import secrets

from typing import Any

from django.core.management.base import BaseCommand
from termcolor import cprint

from utils.parseenv import EnvFile

env = environ.Env(
    AWS_REGION=(str, ""),
    AWS_PLATFORM=(str, ""),
    APP_NAME=(str, ""),
    CLOUD_ENV_FILE=(str, ".env.cloud"),
)


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
            env("AWS_PLATFORM"),
            "--region",
            env("AWS_REGION"),
            env("APP_NAME"),
        ]

        try:
            subprocess.run(
                command,
                check=True,
            )
        except subprocess.CalledProcessError as e:
            cprint(f"Failed to setup AWS Elastic Beanstalk application, Error: {e}", "red")
        else:
            cprint("Setup AWS Elastic Beanstalk application", "green")

    def _setup_enviroment(self) -> None:
        env_file = EnvFile(env("CLOUD_ENV_FILE"))
        command = [
            "eb",
            "create",
            f"{env('APP_NAME')}-dev",
            "--single",
            "--cname",
            f"{env('APP_NAME')}-dev",
            "--envvars",
            env_file.as_string(),
            "--database",
            "--database.engine",
            "mysql",
            "--database.username",
            "ebroot",
            "--database.password",
            secrets.token_urlsafe(16),
        ]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            cprint(f"Failed to setup AWS Elastic Beanstalk environment, Error: {e}", "red")
        else:
            cprint("Setup AWS Elastic Beanstalk environment", "green")


# if __name__ == "__main__":
#     setup()
