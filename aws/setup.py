import subprocess
import os
import sys
import secrets

import parseenv

AWS_REGION = os.environ.get("AWS_REGION")
AWS_PLATFORM = os.environ.get("AWS_PLATFORM")
AWS_ENV_FILE = os.environ.get("AWS_ENV_FILE")
APP_NAME = os.environ.get("APP_NAME")


def main() -> None:
    validate_env_vars()
    setup_app()
    setup_enviroment()


def validate_env_vars() -> None:
    env_vars = ["AWS_REGION", "AWS_PLATFORM", "APP_NAME", "AWS_ENV_FILE"]

    for var in env_vars:
        if not globals().get(var):
            print(f"Please set {var} environment variable.")
            sys.exit(1)


def setup_app() -> None:
    subprocess.run(
        ["eb", "init", "--platform", AWS_PLATFORM, "--region", AWS_REGION, APP_NAME],
        check=True,
    )


def setup_enviroment() -> None:
    env_vars = parseenv.as_string(AWS_ENV_FILE)
    command = [
        "eb",
        "create",
        f"{APP_NAME}-dev",
        "--single",
        "--cname",
        f"{APP_NAME}-dev",
        "--envvars",
        env_vars,
        "--database",
        "--database.engine",
        "mysql",
        "--database.username",
        "ebroot",
        "--database.password",
        secrets.token_urlsafe(16),
        
    ]
    subprocess.run(command, check=True)


if __name__ == "__main__":
    main()
