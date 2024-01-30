from termcolor import cprint
import subprocess

from django.conf import settings
from django.core.management.base import BaseCommand

from utils.env import EnvFile


class Command(BaseCommand):
    help = "Set environment variables in AWS Elastic Beanstalk"

    def handle(self, *args, **options):
        env_vars = EnvFile(settings.ENV("CLOUD_ENV_FILE")).as_list()
        command = ["eb", "setenv"]

        try:
            subprocess.run(command + env_vars, check=True)
        except subprocess.CalledProcessError:
            cprint(
                "Failed to set environment variables in AWS Elastic Beanstalk", "red"
            )
        else:
            cprint("Set environment variables in AWS Elastic Beanstalk", "green")
